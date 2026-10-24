#!/usr/bin/env python3
"""
예상 시험 질문 평가 세트(tools/eval/eval_set.json)로 답안을 기계 채점하고, 허브(llms.txt)만으로
각 문항의 근거 파트를 찾아갈 수 있는지 점검한다.

    python3 tools/eval_grade.py --template answers.md   # 답안 틀 생성(문항마다 '## Q1' 절)
    python3 tools/eval_grade.py answers.md              # 채점: 키워드 커버리지·출처 인용·점수 표
    python3 tools/eval_grade.py --routing               # 허브 라우팅 점검(라우팅 용어·근거 URL이 허브에 있는가)
    python3 tools/eval_grade.py --judge Q7              # ChatGPT에 보낼 채점 프롬프트 출력
    python3 tools/eval_grade.py --list                  # 문항 목록

답안 파일 형식: '## Q1', '## Q2' … 제목 아래에 답을 붙여 넣는다(JSON {"Q1": "..."} 도 가능).
키워드 채점은 핵심 용어의 포함 여부만 보는 거친 척도이므로, 사람이 docs/compiled/rubric.md 의
10점 기준으로 다시 본다.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVAL_SET = ROOT / "tools" / "eval" / "eval_set.json"
HUB = ROOT / "llms.txt"
RUBRIC_URL = "https://raw.githubusercontent.com/dkdlqoddi/study-arrangement/main/docs/compiled/rubric.md"

# 답안·키워드 양쪽에 같은 정규화를 적용해 기호 표기 차이(−/-, ∣/|, 전각 공백 등)를 흡수한다
_NORMALIZE = str.maketrans({"−": "-", "–": "-", "—": "-", "∣": "|", "　": " ", "‖": "||", "ᵀ": "T", "ʼ": "'", "’": "'"})


def load_eval_set(path: Path = EVAL_SET) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(text: str) -> str:
    t = text.translate(_NORMALIZE).lower()
    t = re.sub(r"\s+", " ", t)
    return t


def _contains(text_norm: str, text_nospace: str, term: str) -> bool:
    k = normalize(term)
    if not k:
        return False
    return k in text_norm or k.replace(" ", "") in text_nospace


def keyword_hit(answer: str, group: str) -> bool:
    """'a|b|c' 동의어 그룹 중 하나라도 답안에 있으면 충족."""
    text_norm = normalize(answer)
    text_nospace = text_norm.replace(" ", "")
    return any(_contains(text_norm, text_nospace, alt) for alt in group.split("|") if alt.strip())


def citation_hit(answer: str, item: dict) -> bool:
    """근거 차시('8차시')나 절 번호('§2.12', '2.12절')가 답안에 있으면 출처 인용으로 본다."""
    text = normalize(answer)
    for sec in item.get("source_sections", []):
        m = re.match(r"(\d)차시(?:\s*§\s*([\d.\-]+))?", sec)
        if not m:
            continue
        week, num = m.group(1), m.group(2)
        if f"{week}차시" in text or f"week{week}" in text or f"week0{week}" in text:
            return True
        if num and (f"§{num}" in text or f"§ {num}" in text or f"{num}절" in text):
            return True
    return False


def grade_item(item: dict, answer: str) -> dict:
    groups = item["keywords"]
    hits = [g for g in groups if keyword_hit(answer, g)]
    misses = [g for g in groups if g not in hits]
    coverage = len(hits) / len(groups) if groups else 0.0
    cite = 1.0 if citation_hit(answer, item) else 0.0
    score = item["points"] * (0.75 * coverage + 0.25 * cite)
    return dict(id=item["id"], coverage=coverage, hits=len(hits), total=len(groups), cite=bool(cite),
                score=round(score, 2), points=item["points"], misses=misses)


def parse_answers(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return {k: str(v) for k, v in json.loads(text).items()}
    answers: dict[str, str] = {}
    cur = None
    buf: list[str] = []
    for ln in text.splitlines():
        m = re.match(r"^##\s+(Q\d+)\b", ln.strip())
        if m:
            if cur:
                answers[cur] = "\n".join(buf).strip()
            cur, buf = m.group(1), []
        elif cur:
            buf.append(ln)
    if cur:
        answers[cur] = "\n".join(buf).strip()
    return answers


def write_template(path: Path, data: dict) -> None:
    lines = ["# 답안 (ChatGPT 답 또는 내 답을 각 문항 아래에 붙여 넣기)", "",
             "> 채점: `python3 tools/eval_grade.py " + path.name + "` · 기준: docs/compiled/rubric.md", ""]
    for it in data["items"]:
        lines += [f"## {it['id']} — {it['topic']} ({it['grade']}급 · {it['points']}점)", "",
                  f"문제: {it['question']}", "", "(여기에 답안)", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def routing_check(data: dict, hub_text: str) -> list[dict]:
    hub_norm = normalize(hub_text)
    hub_nospace = hub_norm.replace(" ", "")
    base = data["raw_base"]
    results = []
    for it in data["items"]:
        missing_terms = [t for t in it.get("route_terms", []) if not _contains(hub_norm, hub_nospace, t)]
        missing_urls = [s for s in it["sources"] if (base + s) not in hub_text]
        results.append(dict(id=it["id"], ok=not missing_terms and not missing_urls,
                            missing_terms=missing_terms, missing_urls=missing_urls))
    return results


def judge_prompt(item: dict, data: dict) -> str:
    points = "\n".join(f"- {g.split('|')[0]}" for g in item["keywords"])
    return (
        "채점: 다음은 「보건학을 위한 기계학습」 시험 답안이다. 채점표(정확성 4 · 근거/유도 3 · 수업 맥락 2 · 구조 1 = 10점, 감점 항목 포함)로 채점해 줘. "
        f"반드시 허브 {data['hub']} 에서 근거 절({', '.join(item.get('source_sections', []))})을 열어 대조하고, "
        "(1) 항목별 점수와 근거 (2) 빠진 핵심 포인트 (3) 틀린 문장과 교정문 (4) 대조한 출처를 써 줘. 자료에 없는 보충은 [일반]으로 표시해. "
        f"채점표 원문: {RUBRIC_URL}\n"
        f"[문제] {item['question']}\n"
        f"[반드시 들어가야 할 포인트]\n{points}\n"
        "[내 답안]\n(여기에 붙여 넣기)\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("answers", nargs="?", help="답안 파일(.md 또는 .json)")
    ap.add_argument("--template", metavar="PATH", help="답안 틀을 이 경로에 생성")
    ap.add_argument("--routing", action="store_true", help="허브 라우팅 점검")
    ap.add_argument("--judge", metavar="QID", help="해당 문항의 ChatGPT 채점 프롬프트 출력")
    ap.add_argument("--list", action="store_true", help="문항 목록 출력")
    ap.add_argument("--eval-set", default=str(EVAL_SET))
    args = ap.parse_args()

    data = load_eval_set(Path(args.eval_set))
    items = {it["id"]: it for it in data["items"]}

    if args.list:
        for it in data["items"]:
            print(f"{it['id']:>4} {it['grade']} {it['points']}점  {it['topic']}  ← {', '.join(it['source_sections'])}")
        return 0

    if args.template:
        write_template(Path(args.template), data)
        print(f"답안 틀 생성: {args.template} ({len(data['items'])}문항)")
        return 0

    if args.routing:
        if not HUB.exists():
            print("llms.txt 가 없습니다. python3 tools/convert_sources.py --index-only 로 먼저 생성하세요.")
            return 1
        res = routing_check(data, HUB.read_text(encoding="utf-8"))
        bad = [r for r in res if not r["ok"]]
        print(f"허브 라우팅 점검: {len(res)}문항 중 통과 {len(res) - len(bad)}개, 실패 {len(bad)}개")
        for r in bad:
            print(f"  {r['id']}: 허브에 없는 라우팅 용어 {r['missing_terms']} · 없는 URL {r['missing_urls']}")
        return 1 if bad else 0

    if args.judge:
        it = items.get(args.judge.upper())
        if not it:
            print("없는 문항:", args.judge, "— --list 로 확인")
            return 1
        print(judge_prompt(it, data))
        return 0

    if not args.answers:
        ap.print_help()
        return 1

    answers = parse_answers(Path(args.answers))
    rows = []
    for it in data["items"]:
        ans = answers.get(it["id"], "")
        rows.append(grade_item(it, ans) if ans.strip() else dict(id=it["id"], coverage=0.0, hits=0, total=len(it["keywords"]),
                                                                  cite=False, score=0.0, points=it["points"], misses=["(답안 없음)"]))
    got = sum(r["score"] for r in rows)
    tot = sum(r["points"] for r in rows)
    print(f"{'문항':<5}{'키워드':>8}  {'출처':<4}{'점수':>9}  빠진 키워드(동의어 그룹의 첫 항목)")
    for r in rows:
        miss = ", ".join(m.split("|")[0] for m in r["misses"][:4])
        print(f"{r['id']:<5}{r['hits']:>3}/{r['total']:<4}  {'O' if r['cite'] else '-':<4}{r['score']:>5.2f}/{r['points']:<3}  {miss}")
    print(f"\n총점 {got:.2f}/{tot} = {100 * got / tot:.1f}점 (100점 환산) · 답안이 있는 문항 {sum(1 for r in rows if r['misses'] != ['(답안 없음)'])}/{len(rows)}")
    print("7점(70%) 이상인 문항도 docs/compiled/rubric.md 1절 기준으로 사람이 다시 봅니다.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
