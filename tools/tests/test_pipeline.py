"""
변환 파이프라인 단위 테스트.  실행: python3 -m pytest tools/tests -q
원본 자료가 없어도 돌아가도록 합성 입력만 쓴다.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import pdfmd  # noqa: E402
import convert_sources as cs  # noqa: E402


# ---------------------------------------------------------------- pdfmd
def test_joiner_latin_space_and_punctuation():
    assert pdfmd.joiner("Prediction", "vs Inference") == " "
    assert pdfmd.joiner("유연성-", "해석력") == ""
    assert pdfmd.joiner("값", ", 그리고") == ""
    assert pdfmd.joiner("최적 예측자", "E[Y|X]") == " "


def test_joiner_hangul_uses_word_boundary_model():
    # 단어 중간에서 끊긴 경우는 붙이고, 단어 사이에서 끊긴 경우는 띄운다
    assert pdfmd.joiner("Chap2까지 진행됐", "다. 녹음은") == ""
    assert pdfmd.joiner("ISLR 순서를", "따라가며 10주차쯤") == " "


def test_join_lines_keeps_bullets_separate():
    out = pdfmd.join_lines(["• 첫 항목", "이어지는 줄", "• 둘째 항목"])
    assert out.splitlines() == ["- 첫 항목이어지는 줄", "- 둘째 항목"] or out.count("\n") == 1


def test_real_table_filter():
    assert pdfmd._real_table([["항목", "Statistics", "ML"], ["주 관심", "가설검정", "예측"]])
    assert not pdfmd._real_table([["긴 글 " * 100, "긴 글 " * 100]])  # 색 박스 오인
    same = "슬라이드 원문 — 같은 글"
    assert not pdfmd._real_table([["Col1", "Col2", "Col3"], [same, same, same]])
    assert not pdfmd._real_table([["하나"], ["둘"]])  # 열 하나


def test_needs_respace():
    assert pdfmd._needs_respace("연구분야에따라서머신러닝보다는통계학습이라고도함")
    assert not pdfmd._needs_respace("연구 분야에 따라서 machine learning 보다는 statistical learning 이라고도 함.")
    assert not pdfmd._needs_respace("짧은글")


# ---------------------------------------------------------- convert_sources
def test_split_md_respects_budget_and_keeps_content():
    sections = []
    for i in range(12):
        sections.append(f"## 절 {i}\n\n" + ("문장 하나. " * 400) + "\n")
    md = "\n".join(sections)
    parts = cs.split_md(md, 3000)
    assert len(parts) > 1
    assert all(cs.tokens(p) <= 3000 for p in parts)
    joined = "".join(parts).replace("\n", "")
    assert joined.count("## 절") == 12
    assert all(p.lstrip().startswith("## 절") for p in parts)  # 제목 경계에서 잘림


def test_scrub_pii_email_phone_and_redact(monkeypatch):
    monkeypatch.setattr(cs, "REDACT", [("홍길동", "[발표자]")])
    text = "문의 abc.def@snu.ac.kr 또는 010-1234-5678. 발표자 홍길동, 띄어진 홍 길 동. 수치 0206554 <0001 은 그대로."
    out = cs.scrub_pii(text)
    assert "abc.def" not in out and "[이메일 제거]" in out
    assert "010-1234-5678" not in out and "[전화번호 제거]" in out
    assert "홍길동" not in out and "홍 길 동" not in out and out.count("[발표자]") == 2
    assert "0206554" in out  # OCR 숫자열은 전화번호로 오인하지 않음


def test_hub_heading_cleanup(tmp_path, monkeypatch):
    doc = tmp_path / "docs" / "weekXX" / "a_part01.md"
    doc.parent.mkdir(parents=True)
    doc.write_text(
        "# 제목\n\n---\n## ML for Health Science 5차시 시험 대비 학습자료 (요약본)\n"
        "### 2. 핵심 개념 정리\n#### 2.1 LDA p=1 — 판별점수 (S27–S30, 칠판 19:22)\n#### 2.2 p>1 — 다변량 정규 (S31)\n",
        encoding="utf-8")
    monkeypatch.setattr(cs, "ROOT", tmp_path)
    heads = cs._hub_headings("docs/weekXX/a_part01.md", 70)
    assert heads == ["2. 핵심 개념 정리", "2.1 LDA p=1 — 판별점수", "2.2 p>1 — 다변량 정규"]


def test_resolve_section_points_to_part_with_heading(tmp_path, monkeypatch):
    d = tmp_path / "docs" / "weekXX"
    d.mkdir(parents=True)
    (d / "study_guide_summary.md").write_text("# 목차\n", encoding="utf-8")
    (d / "study_guide_summary_part01.md").write_text("#### 2.1 하나\n#### 2.2 둘\n", encoding="utf-8")
    (d / "study_guide_summary_part02.md").write_text("### 3. 용어 정리\n#### 2.10 열\n", encoding="utf-8")
    monkeypatch.setattr(cs, "ROOT", tmp_path)
    assert cs._resolve_section("docs/weekXX/study_guide_summary.md", "2.2").endswith("part01.md")
    assert cs._resolve_section("docs/weekXX/study_guide_summary.md", "2.10").endswith("part02.md")
    assert cs._resolve_section("docs/weekXX/study_guide_summary.md", "3").endswith("part02.md")
    assert cs._resolve_section("docs/weekXX/study_guide_summary.md", None).endswith("part01.md")


def test_public_categories_are_only_summary_and_compiled():
    assert cs.PUBLIC_CATEGORIES == {"study_guide_summary", "compiled"}
    assert cs.is_public({"category": "study_guide_summary"})
    assert not cs.is_public({"category": "transcripts"})


def test_header_reserve_keeps_parts_under_limit():
    assert cs.HEADER_RESERVE >= 300 and cs.HUB_BUDGET_TOKENS <= cs.MAX_TOKENS
