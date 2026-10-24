"""
PDF → Markdown 변환기 (pymupdf 기반).

* 글꼴 크기·굵기로 제목 단계 복원
* 줄 간격(gap / 글자 크기)으로 문단 경계 판단 → PDF 줄바꿈을 한 문단으로 합침
* 표: page.find_tables() 결과 중 진짜 표만 골라 markdown 표로
* 이미지 전용 페이지: rapidocr(한국어+영어 모델)로 OCR
"""
from __future__ import annotations

import re
from collections import Counter

import pymupdf

OCR_MIN_CHARS = 40          # 추출 텍스트가 이보다 짧으면 이미지 전용 페이지로 보고 OCR
PARA_GAP_RATIO = 0.29       # (다음 줄 y0 - 이전 줄 y1) / 글자크기 가 이 값 미만이면 같은 문단
HANGUL = re.compile(r"[\uac00-\ud7a3\u3131-\u318e]")
BULLET_RE = re.compile(r"^(?:[•▪■□○●◦‣⁃➢➤►▶·]\s*|[-–]\s+|\(?\d{1,2}[.)]\s+|[①-⑳]\s*|[☐☑✓✔]\s*|[a-zA-Z][.)]\s+)")
ONENOTE_FOOTER = re.compile(r"^(Machine_learning_for_Health_Science|Topics_in_Biochemical_Engineering)\s*페이지\s*\d+\s*$")
DIGITS_ONLY = re.compile(r"^[\d\s/.\-–]+$")


# ---------------------------------------------------------------------------
# 한국어 띄어쓰기 복원 (kiwipiepy). 없으면 조용히 건너뜀.
_kiwi = None
_kiwi_failed = False


def _get_kiwi():
    global _kiwi, _kiwi_failed
    if _kiwi is None and not _kiwi_failed:
        try:
            from kiwipiepy import Kiwi
            _kiwi = Kiwi()
        except Exception:
            _kiwi_failed = True
    return _kiwi


def korean_respace(text: str) -> str:
    """띄어쓰기가 사라진 한국어 문장(OneNote 내보내기, OCR)에 공백을 복원. 기존 공백은 유지."""
    kiwi = _get_kiwi()
    if kiwi is None or len(HANGUL.findall(text)) < 2:
        return text
    try:
        out = kiwi.space(text, reset_whitespace=False)
    except Exception:
        return text
    out = re.sub(r"\s*·\s*", "·", out)
    out = re.sub(r"\s+([,.)\]」”:;!?%])", r"\1", out)
    return out


LONG_HANGUL_RUN = re.compile(r"[가-힣]{12,}")


def _needs_respace(text: str) -> bool:
    """띄어쓰기가 사라진 텍스트인지: 한글 6자 이상인데 공백이 거의 없거나, 12자 이상 붙은 한글 덩어리가 있으면 True."""
    h = len(HANGUL.findall(text))
    if h < 6:
        return False
    return text.count(" ") < h * 0.08 or bool(LONG_HANGUL_RUN.search(text))


def _space_at_boundary(a: str, b: str) -> bool:
    """a 와 b 를 이어 붙였을 때 kiwi 가 경계에 공백을 넣는지(= 원래 띄어 쓴 단어 경계인지)."""
    kiwi = _get_kiwi()
    if kiwi is None:
        return False
    tail = a.rsplit(" ", 1)[-1][-12:]
    head = b.split(" ", 1)[0][:12]
    if not tail or not head:
        return False
    try:
        s = kiwi.space(tail + head, reset_whitespace=False)
    except Exception:
        return False
    n = len(tail.replace(" ", ""))
    cnt = 0
    for i, ch in enumerate(s):
        if ch != " ":
            cnt += 1
            if cnt == n:
                return i + 1 < len(s) and s[i + 1] == " "
    return False


def joiner(prev: str, nxt: str) -> str:
    """두 줄을 한 문단으로 합칠 때 사이에 넣을 문자.
    한글-한글 경계는 PDF 줄바꿈이 단어 중간인지 단어 사이인지 알 수 없으므로 kiwi 로 판단."""
    if not prev or not nxt:
        return ""
    a, b = prev[-1], nxt[0]
    if a in "-–(［[「“\"'/·":
        return ""
    if b in ",.)]」”:;!?%":
        return ""
    if HANGUL.match(a) and HANGUL.match(b):
        return " " if _space_at_boundary(prev, nxt) else ""
    return " "


def clean_text(s: str) -> str:
    s = s.replace("\u00a0", " ").replace("\u200b", "").replace("\x00", "")
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip()


def md_escape_cell(s: str) -> str:
    return s.replace("|", "\\|").replace("\n", " ").strip()


def normalize_bullet(ln: str) -> str:
    ln = re.sub(r"^[•▪■●‣⁃➢➤►▶]\s*", "- ", ln)
    ln = re.sub(r"^[○◦□]\s*", "  - ", ln)
    ln = re.sub(r"^☐\s*", "- [ ] ", ln)
    ln = re.sub(r"^[☑✓✔]\s*", "- [x] ", ln)
    return ln


def join_lines(lines: list[str]) -> str:
    """줄 리스트 → 한 문단(불릿 줄은 새 줄 유지)."""
    out: list[str] = []
    for ln in lines:
        ln = clean_text(ln)
        if not ln:
            continue
        if BULLET_RE.match(ln) or not out:
            out.append(ln)
        else:
            out[-1] = out[-1] + joiner(out[-1], ln) + ln
    return "\n".join(normalize_bullet(x) for x in out)


# ---------------------------------------------------------------------------
# OCR
# ---------------------------------------------------------------------------
_ocr = None
_ocr_kind = None


def _get_ocr():
    global _ocr, _ocr_kind
    if _ocr is not None:
        return _ocr
    try:
        from rapidocr import RapidOCR, LangRec, ModelType, OCRVersion
        _ocr = RapidOCR(params={"Rec.lang_type": LangRec.KOREAN, "Rec.model_type": ModelType.MOBILE,
                                "Rec.ocr_version": OCRVersion.PPOCRV4})
        _ocr_kind = "rapidocr-korean"
    except Exception:
        from rapidocr_onnxruntime import RapidOCR
        _ocr = RapidOCR()
        _ocr_kind = "rapidocr_onnxruntime"
    return _ocr


def ocr_page(page, dpi: int = 200) -> list[str]:
    eng = _get_ocr()
    pix = page.get_pixmap(dpi=dpi)
    png = pix.tobytes("png")
    boxes = []
    if _ocr_kind == "rapidocr-korean":
        res = eng(png)
        if res is None or not res.txts:
            return []
        for box, txt, conf in zip(res.boxes, res.txts, res.scores):
            xs = [float(p[0]) for p in box]
            ys = [float(p[1]) for p in box]
            boxes.append((min(ys), max(ys), min(xs), txt.strip(), float(conf)))
    else:
        res, _ = eng(png)
        if not res:
            return []
        for box, txt, conf in res:
            xs = [p[0] for p in box]
            ys = [p[1] for p in box]
            boxes.append((min(ys), max(ys), min(xs), txt.strip(), float(conf)))
    if not boxes:
        return []
    med_h = sorted(b[1] - b[0] for b in boxes)[len(boxes) // 2] or 10
    boxes.sort(key=lambda b: (b[0], b[2]))
    lines: list[list] = []
    for b in boxes:
        if lines and abs(b[0] - lines[-1][0][0]) < med_h * 0.6:
            lines[-1].append(b)
        else:
            lines.append([b])
    out = []
    for ln in lines:
        ln.sort(key=lambda b: b[2])
        txt = " ".join((b[3] + (" (?)" if b[4] < 0.6 else "")) for b in ln if b[3])
        if txt:
            out.append(txt)
    return out


# ---------------------------------------------------------------------------
def _span_bold(s) -> bool:
    return bool(s["flags"] & 16) or "bold" in s["font"].lower()


def _real_table(rows: list[list[str]]) -> bool:
    if len(rows) < 2 or max(len(r) for r in rows) < 2:
        return False
    cells = [c for r in rows for c in r]
    nonempty = [c for c in cells if c]
    if len(nonempty) < 0.5 * len(cells):
        return False
    if max(len(c) for c in nonempty) > 400:
        return False
    for r in rows:
        ne = [c for c in r if c]
        if len(ne) >= 2 and len(set(ne)) == 1:
            return False  # 같은 글이 모든 칸에 반복 → 색 박스를 표로 오인
    return True


def _extract_tables(page):
    tables = []
    try:
        found = page.find_tables()
    except Exception:
        return tables
    for t in found.tables:
        try:
            rows_raw = t.extract()
        except Exception:
            continue
        rows = [[join_lines((c or "").split("\n")).replace("\n", " ") for c in r] for r in rows_raw]
        if not _real_table(rows):
            continue
        ncol = max(len(r) for r in rows)
        md = []
        for i, r in enumerate(rows):
            r = r + [""] * (ncol - len(r))
            md.append("| " + " | ".join(md_escape_cell(c) for c in r) + " |")
            if i == 0:
                md.append("|" + " --- |" * ncol)
        tables.append((tuple(t.bbox), "\n".join(md)))
    # 겹치는 표(큰 박스 안의 표)는 작은 쪽만 남김
    keep = []
    for bb, md in tables:
        inner = any(o is not bb and bb[0] <= o[0] and bb[1] <= o[1] and bb[2] >= o[2] and bb[3] >= o[3]
                    for o, _ in tables)
        if not inner:
            keep.append((bb, md))
    return keep


def pdf_to_md(path, mode: str, pages: list[int] | None = None, use_ocr: bool = True,
              page_label: str = "p.") -> tuple[str, dict]:
    """
    mode = "doc"    : 연속 문서(학습자료). 제목 복원 + 표 추출, 페이지 경계는 HTML 주석.
    mode = "slides" : 페이지(슬라이드)마다 '## 슬라이드 N'.
    mode = "notes"  : 페이지마다 '## 노트 p.N'.
    이미지 전용 페이지는 OCR.
    """
    doc = pymupdf.open(path)
    page_idx = list(range(len(doc))) if pages is None else pages
    stats = {"pages": len(page_idx), "ocr_pages": 0, "tables": 0, "method": "pdf-text"}

    # 1) 글꼴 통계 → 본문 크기, 제목 크기 단계
    size_chars: Counter = Counter()
    bold_sizes: Counter = Counter()
    for i in page_idx:
        for b in doc[i].get_text("dict")["blocks"]:
            if b.get("type") != 0:
                continue
            for l in b["lines"]:
                for s in l["spans"]:
                    t = s["text"].strip()
                    if not t:
                        continue
                    sz = round(s["size"] * 2) / 2
                    size_chars[sz] += len(t)
                    if _span_bold(s):
                        bold_sizes[sz] += len(t)
    body = size_chars.most_common(1)[0][0] if size_chars else 10.0
    heading_sizes = sorted({sz for sz in bold_sizes if sz >= body * 1.12 and sz >= body + 0.9}, reverse=True)
    if mode != "doc":
        heading_sizes = heading_sizes[:1]
    level_of = {sz: min(2 + k, 5) for k, sz in enumerate(heading_sizes)}

    out: list[str] = []
    for i in page_idx:
        page = doc[i]
        pno = i + 1
        ph = page.rect.height
        d = page.get_text("dict")
        text_blocks = [b for b in d["blocks"] if b.get("type") == 0]
        img_blocks = [b for b in d["blocks"] if b.get("type") == 1]
        plain = page.get_text().strip()
        plain_wo_footer = "\n".join(ln for ln in plain.splitlines() if not ONENOTE_FOOTER.match(ln.strip())).strip()

        if mode == "slides":
            out.append(f"\n## 슬라이드 {pno}\n")
        elif mode == "notes":
            out.append(f"\n## 노트 {page_label}{pno}\n")
        else:
            out.append(f"\n<!-- page {pno} -->\n")

        # 2) 이미지 전용 페이지 → OCR
        if len(plain_wo_footer) < OCR_MIN_CHARS:
            if use_ocr and (img_blocks or page.get_images()):
                lines = ocr_page(page)
                stats["ocr_pages"] += 1
                stats["method"] = "pdf-text+ocr"
                if lines:
                    out.append("_(이미지 기반 페이지 → OCR 추출 텍스트, 오탈자·수식 깨짐 가능)_\n")
                    lines = [korean_respace(x) if len(HANGUL.findall(x)) >= 4 else x for x in lines]
                    out.append(join_lines(lines))
                else:
                    out.append("_(이미지 전용 페이지 — OCR로 읽은 텍스트 없음)_")
            elif plain_wo_footer:
                out.append(join_lines(plain_wo_footer.splitlines()))
            else:
                out.append("_(이미지 전용 페이지 — 텍스트 없음)_")
            continue

        # 3) 표
        tables = _extract_tables(page) if mode == "doc" else []
        stats["tables"] += len(tables)

        def in_table(bb):
            cx, cy = (bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2
            return any(x0 - 1 <= cx <= x1 + 1 and y0 - 1 <= cy <= y1 + 1 for (x0, y0, x1, y1), _ in tables)

        # 4) 줄 수집 (표 안 제외, 푸터 제외)
        lines = []  # (y0, x0, y1, size, bold, text)
        for b in text_blocks:
            for l in b["lines"]:
                raw = "".join(s["text"] for s in l["spans"])
                txt = clean_text(raw)
                if not txt or ONENOTE_FOOTER.match(txt):
                    continue
                if in_table(l["bbox"]):
                    continue
                spans = [s for s in l["spans"] if s["text"].strip()] or l["spans"]
                s0 = max(spans, key=lambda s: len(s["text"].strip()))  # 글자 수가 가장 많은 span 기준(불릿 기호 글꼴 무시)
                sz = round(s0["size"] * 2) / 2
                bold = all(_span_bold(s) for s in spans if len(s["text"].strip()) > 1) and _span_bold(s0)
                y0, y1 = l["bbox"][1], l["bbox"][3]
                if DIGITS_ONLY.match(txt) and (mode == "slides" or y0 < 40 or y1 > ph - 45):
                    continue  # 쪽번호/슬라이드 번호
                lines.append([y0, l["bbox"][0], y1, sz, bold, txt])
        lines.sort(key=lambda r: (round(r[0]), r[1]))

        # 같은 높이에 있는 조각들은 한 줄로 합침
        merged = []
        for r in lines:
            if merged and abs(r[0] - merged[-1][0]) < 2.0 and r[1] >= merged[-1][1]:
                m = merged[-1]
                m[5] = m[5] + " " + r[5]
                m[2] = max(m[2], r[2])
                m[4] = m[4] and r[4]
            else:
                merged.append(list(r))

        # 5) 문단 묶기
        elements: list[tuple[float, str]] = []
        for bb, md in tables:
            elements.append((bb[1], md))

        para: list[str] = []
        para_y = None
        prev = None

        def flush():
            nonlocal para, para_y
            if para:
                text = join_lines(para)
                if mode == "notes" or _needs_respace(text):
                    # OneNote 내보내기·일부 PDF는 한국어 띄어쓰기가 사라져 있음 → 복원
                    text = "\n".join(korean_respace(x) for x in text.split("\n"))
                elements.append((para_y, text))
            para, para_y = [], None

        for r in merged:
            y0, x0, y1, sz, bold, txt = r
            is_heading = sz in level_of and bold
            is_label = (not is_heading) and bold and len(txt) <= 80 and sz < body * 1.12
            if is_heading:
                flush()
                hl = "#" * level_of[sz] + " "
                # 두 줄로 나뉜 제목 이어붙이기
                if elements and elements[-1][1].startswith(hl) and prev is not None and prev[3] == sz \
                        and (y0 - prev[2]) / sz < 0.6 and not re.match(r"^\d+(\.\d+)*\.?\s", txt):
                    y, h = elements[-1]
                    elements[-1] = (y, h + joiner(h, txt) + txt)
                else:
                    elements.append((y0, hl + txt))
            elif is_label:
                flush()
                # 바로 앞 라벨의 확장(예: '교수님 말씀 · 강의노트' → '교수님 말씀 · 강의노트 p.3')이면 대체
                if elements and elements[-1][1].startswith("**") and txt.startswith(elements[-1][1].strip("*")) \
                        and prev is not None and (y0 - prev[2]) / sz < 1.6:
                    elements[-1] = (elements[-1][0], f"**{txt}**")
                else:
                    elements.append((y0, f"**{txt}**"))
            else:
                new_para = True
                if para and prev is not None:
                    gap = (y0 - prev[2]) / max(prev[3], 1)
                    same_size = abs(sz - prev[3]) <= 1.0
                    if gap < PARA_GAP_RATIO and same_size and not BULLET_RE.match(txt):
                        new_para = False
                if new_para:
                    flush()
                    para_y = y0
                para.append(txt)
            prev = r
        flush()

        if mode == "doc":
            last_img_y = -1e9
            for b in img_blocks:
                bb = b["bbox"]
                if bb[3] - bb[1] > 100 and bb[1] - last_img_y > 30:
                    elements.append((bb[1], f"_[그림/슬라이드 이미지 — 원본 PDF p.{pno} 참고]_"))
                    last_img_y = bb[1]

        elements.sort(key=lambda e: e[0])
        out.append("\n\n".join(e[1].strip() for e in elements if e[1].strip()))

    md = "\n".join(out)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    return md, stats
