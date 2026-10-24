"""
시험 대비 문서(예상 질문·프롬프트 북·채점표)와 평가 세트·채점 도구의 일관성 테스트.
실행: tools/run_tests.sh  (또는 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python3 -m pytest tools/tests -q)

빌드 산출물(docs/compiled/*, llms.txt, docs/manifest.json)이 있어야 하는 테스트는 산출물이 없으면 건너뛴다.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import convert_sources as cs  # noqa: E402
import eval_grade as eg  # noqa: E402

ROOT = cs.ROOT
CONTENT = ROOT / "tools" / "content"
PRED = CONTENT / "exam_predictions.md"
PROMPTS = CONTENT / "prompt_book.md"
RUBRIC = CONTENT / "rubric.md"
HUB = ROOT / "llms.txt"
MANIFEST = ROOT / "docs" / "manifest.json"

Q_RE = re.compile(r"^\*\*Q(\d+) \[([ABC])·([^\]]+)\] (.+)\*\*$")
N_QUESTIONS = 42


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def _questions(text: str) -> list[dict]:
    """예상 질문 문서를 Q 블록 단위로 나눈다: {n, grade, type, stem, body}."""
    out, cur = [], None
    for ln in text.splitlines():
        m = Q_RE.match(ln.strip())
        if m:
            cur = dict(n=int(m.group(1)), grade=m.group(2), type=m.group(3), stem=m.group(4), body=[])
            out.append(cur)
        elif cur is not None:
            if ln.startswith("## "):
                cur = None
            else:
                cur["body"].append(ln)
    return out


def _section_refs(line: str) -> list[tuple[int, str]]:
    """'8차시 §2.12(…), 7차시 §2.11–2.13, §2.5' → [(8,'2.12'), (7,'2.11'), (7,'2.5')] — 차시가 생략되면 직전 차시를 따른다."""
    refs, week = [], None
    for tok in re.finditer(r"(\d)차시|§\s*(\d+(?:[.\-]\d+)?)", line):
        if tok.group(1):
            week = int(tok.group(1))
        elif week is not None:
            refs.append((week, tok.group(2)))
    return refs


def _heading_exists(week: int, section: str) -> bool:
    wdir = next(iter(sorted((ROOT / "docs").glob(f"week{week:02d}_*"))), None)
    if wdir is None:
        return False
    pat = re.compile(r"^#{2,4}\s+" + re.escape(section) + (r"(?!\d)" if ("." in section or "-" in section) else r"\.(?!\d)"))
    for part in sorted(wdir.glob("study_guide_summary*.md")):
        if any(pat.match(ln) for ln in _read(part).splitlines()):
            return True
    return False


# ------------------------------------------------------------------ 내용 파일 구조
def test_prediction_questions_are_numbered_and_complete():
    qs = _questions(_read(PRED))
    assert [q["n"] for q in qs] == list(range(1, N_QUESTIONS + 1))
    for q in qs:
        body = "\n".join(q["body"])
        assert "- 답안 핵심:" in body, q["n"]
        assert "- 근거:" in body, q["n"]
        assert re.search(r"- 프롬프트: Q%d\b" % q["n"], body), q["n"]
    assert sum(q["grade"] == "A" for q in qs) >= 15  # A급이 충분히 있어야 '집중' 문서로서 의미가 있다


def test_prediction_sources_resolve_to_real_sections():
    missing = []
    for q in _questions(_read(PRED)):
        for ln in q["body"]:
            if ln.startswith("- 근거:"):
                for week, sec in _section_refs(ln):
                    if not _heading_exists(week, sec):
                        missing.append((q["n"], week, sec))
    assert not missing, f"요약본에 없는 절 참조: {missing}"


def test_every_question_has_matching_prompt_and_vice_versa():
    pred_ids = {q["n"] for q in _questions(_read(PRED))}
    prompt_ids = {int(m) for m in re.findall(r"^- \*\*Q(\d+)\*\* →", _read(PROMPTS), flags=re.M)}
    assert prompt_ids == pred_ids
    for pid in range(1, 10):
        assert f"**P{pid} " in _read(PROMPTS), pid


def test_prompts_point_to_hub_and_rubric():
    text = _read(PROMPTS)
    blocks = re.findall(r"```\n(.*?)```", text, flags=re.S)
    assert blocks, "P0 코드 블록이 없다"
    p0 = blocks[0]
    assert cs.RAW_BASE + "llms.txt" in p0
    assert "rubric.md" in p0
    assert "표준화" in p0 and "재적합" in p0 and "격자" in p0  # 교수님 점검 항목
    assert cs.RAW_BASE + "docs/compiled/formulas.md" in text


def test_rubric_mock_exam_points_add_up():
    text = _read(RUBRIC)
    a = [int(x) for x in re.findall(r"^\*\*A\d+\. \((\d+)점", text, flags=re.M)]
    b = [int(x) for x in re.findall(r"^\*\*B\d+\. \((\d+)점", text, flags=re.M)]
    assert len(a) == 10 and sum(a) == 100, a
    assert len(b) == 4 and sum(b) == 50, b


def test_readme_contains_identical_master_prompt():
    p0 = re.findall(r"```\n(.*?)```", _read(PROMPTS), flags=re.S)[0]
    assert p0 in _read(ROOT / "README.md"), "README의 P0 프롬프트가 프롬프트 북과 다르다"


def test_new_docs_have_no_private_links_or_pii():
    for p in (PRED, PROMPTS, RUBRIC):
        text = _read(p)
        assert "private/" not in text, p.name
        assert cs.scrub_pii(text) == text, f"{p.name}: 이메일·전화번호·실명이 들어 있다"
        for url in re.findall(r"https://raw\.githubusercontent\.com/\S+", text):
            url = url.rstrip(").,·")
            assert url.startswith(cs.RAW_BASE), url


def test_manual_compiled_registers_exam_docs_first():
    names = [t[0] for t in cs.MANUAL_COMPILED]
    assert names[:3] == ["exam_predictions.md", "prompt_book.md", "rubric.md"]
    assert all(t[4] for t in cs.MANUAL_COMPILED[:3]) and not cs.MANUAL_COMPILED[-1][4]
    assert cs.EXAM_MODE and set(cs.EXAM_MODE["docs"]) <= set(names)


# ------------------------------------------------------------------ 빌드 산출물
@pytest.fixture(scope="module")
def manifest():
    if not MANIFEST.exists():
        pytest.skip("docs/manifest.json 없음 — --index-only 먼저")
    return json.loads(_read(MANIFEST))


@pytest.fixture(scope="module")
def hub():
    if not HUB.exists():
        pytest.skip("llms.txt 없음")
    return _read(HUB)


def test_compiled_exam_docs_built_within_limits(manifest):
    by_src = {Path(e["source"]).name: e for e in manifest["compiled"]}
    for name in ("exam_predictions.md", "prompt_book.md", "rubric.md"):
        e = by_src[name]
        assert e["files"], name
        for f in e["files"]:
            assert (ROOT / f["path"]).exists()
            assert f["tokens"] <= manifest["max_tokens"], f
    assert [Path(e["source"]).name for e in manifest["compiled"][:3]] == ["exam_predictions.md", "prompt_book.md", "rubric.md"]


def test_prediction_url_table_points_to_existing_files():
    for url in re.findall(r"https://raw\.githubusercontent\.com/\S+?\.(?:md|txt)", _read(PRED)):
        rel = url[len(cs.RAW_BASE):]
        assert (ROOT / rel).exists(), rel


def test_hub_has_exam_mode_block(manifest, hub):
    assert "## ★ 시험 모드" in hub
    by_src = {Path(e["source"]).name: e for e in manifest["compiled"]}
    for name in cs.EXAM_MODE["docs"]:
        for f in by_src[name]["files"]:
            assert cs.RAW_BASE + f["path"] in hub, f["path"]
    for path, _ in cs.EXAM_MODE["links"]:
        assert cs.RAW_BASE + path in hub and (ROOT / path).exists(), path
    assert cs.tokens(hub) <= cs.HUB_BUDGET_TOKENS
    # 절 제목이 잘리지 않을 만큼 예산 안에 있어야 라우팅이 유지된다(44자까지 줄면 경고)
    assert "2.12 1차원 라쏘의 해 — soft thresholding" in hub


def test_week_readmes_show_exam_focus():
    for w in cs.WEEKS:
        readme = ROOT / "docs" / w["slug"] / "README.md"
        if not readme.exists():
            pytest.skip("주차 README 없음")
        text = _read(readme)
        assert "## 시험 포인트" in text and w["exam_focus"][:20] in text, w["slug"]
        assert "../compiled/exam_predictions.md" in text


# ------------------------------------------------------------------ 평가 세트·채점 도구
@pytest.fixture(scope="module")
def eval_set():
    return eg.load_eval_set()


def test_eval_set_is_consistent(eval_set):
    ids = [it["id"] for it in eval_set["items"]]
    assert len(ids) == len(set(ids)) >= 25
    pred_ids = {f"Q{q['n']}" for q in _questions(_read(PRED))}
    for it in eval_set["items"]:
        assert it["id"] in pred_ids, it["id"]
        assert len(it["keywords"]) >= 4 and all(it["keywords"])
        assert it["points"] > 0 and it["grade"] in "ABC"
        for src in it["sources"]:
            assert (ROOT / src).exists(), src
        for sec in it["source_sections"]:
            m = re.match(r"(\d)차시 §(\d+\.\d+)$", sec)
            if m:
                assert _heading_exists(int(m.group(1)), m.group(2)), sec
    assert sum(it["points"] for it in eval_set["items"]) >= 100


def test_eval_grade_scores_monotone(eval_set):
    item = next(it for it in eval_set["items"] if it["id"] == "Q1")
    full = ("8차시 §2.12: β>0이면 β̂ = y − λ/2, β<0이면 y + λ/2, |y| ≤ λ/2이면 정확히 0 → sgn(y)(|y| − λ/2)₊, "
            "soft thresholding. λ=4: y=−1.5 → 0, y=5 → 3. 능형 해 y/(1+λ)와 비교.")
    partial = "라쏘 해는 soft thresholding이고 작은 값은 정확히 0이 된다."
    empty = "모르겠다."
    s_full, s_part, s_empty = (eg.grade_item(item, a)["score"] for a in (full, partial, empty))
    assert s_full == item["points"] and s_full > s_part > s_empty == 0
    assert eg.grade_item(item, full)["cite"] and not eg.grade_item(item, partial)["cite"]


def test_eval_grade_normalizes_symbols(eval_set):
    item = next(it for it in eval_set["items"] if it["id"] == "Q24")
    ans = "(1-1/n)^n -> 1/e ≈ 0.368, 즉 63%만 포함되고 나머지는 out-of-bag. 예측오차는 cross validation."
    r = eg.grade_item(item, ans)
    assert r["hits"] == r["total"], r["misses"]


def test_parse_answers_markdown(tmp_path):
    f = tmp_path / "answers.md"
    f.write_text("# 답안\n\n## Q1 — 제목\n\n문제: …\n\n첫 답\n둘째 줄\n\n## Q2\n둘째 답\n", encoding="utf-8")
    ans = eg.parse_answers(f)
    assert ans["Q1"].startswith("문제:") and "둘째 줄" in ans["Q1"] and ans["Q2"] == "둘째 답"


def test_hub_routing_terms_present(eval_set, hub):
    res = eg.routing_check(eval_set, hub)
    bad = [r for r in res if not r["ok"]]
    assert not bad, bad
