#!/usr/bin/env python3
"""
칠판 사진(Quick Share/*.jpg) → 비공개 썸네일 + 촬영 시각 + 캡션 표.

    python3 tools/photos.py                 # 썸네일 생성(없는 것만) + README 렌더
    python3 tools/photos.py --render-only   # captions.json 만 다시 읽어 README 렌더

출력: private/docs/weekNN_YYYYMMDD/photos/{<원본이름>.jpg, captions.json, README.md}
captions.json 형식: {"20260916_192620.jpg": "판서 설명 …", ...}  (사람 또는 AI가 채움)
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import os
import re
import sys
from pathlib import Path

from PIL import Image, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parent))
from convert_sources import PRIV_OUT, SRC, WEEKS, scrub_pii  # noqa: E402

MAX_SIDE = 1280
QUALITY = 72
TODAY = dt.date.today().isoformat()


def capture_time(path: Path) -> str:
    try:
        ex = Image.open(path).getexif()
        v = ex.get(36867) or ex.get(306)
        if v:
            return str(v).replace(":", "-", 2)[:19]
    except Exception:
        pass
    m = re.search(r"(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})", path.name)
    if m:
        y, mo, d, h, mi, s = m.groups()
        return f"{y}-{mo}-{d} {h}:{mi}:{s}"
    return ""


def make_thumb(src: Path, dst: Path) -> tuple[int, int]:
    im = Image.open(src)
    im = ImageOps.exif_transpose(im)
    im.thumbnail((MAX_SIDE, MAX_SIDE))
    dst.parent.mkdir(parents=True, exist_ok=True)
    im.convert("RGB").save(dst, "JPEG", quality=QUALITY, optimize=True)
    return im.size


def process_week(w: dict, render_only: bool) -> dict | None:
    folder = SRC / w["folder"] / "Quick Share"
    photos = sorted(glob.glob(str(folder / "*.jpg")))
    if not photos:
        return None
    out_dir = PRIV_OUT / w["slug"] / "photos"
    out_dir.mkdir(parents=True, exist_ok=True)
    caps_path = out_dir / "captions.json"
    captions = json.loads(caps_path.read_text(encoding="utf-8")) if caps_path.exists() else {}
    rows = []
    for p in photos:
        p = Path(p)
        thumb = out_dir / p.name
        if not render_only and not thumb.exists():
            make_thumb(p, thumb)
        rows.append((capture_time(p), p.name, captions.get(p.name, "")))
    rows.sort()
    n_cap = sum(1 for r in rows if r[2])
    lines = [
        f"# {w['n']}차시 ({w['date']}) 칠판 사진 {len(rows)}장 — 비공개",
        "",
        f"> 원본 `machine_learning_for_health_science/{w['folder']}/Quick Share/` 의 사진을 {MAX_SIDE}px 썸네일로 줄인 것. "
        f"촬영 시각은 EXIF 기준. 설명은 사진을 보고 AI가 쓴 것으로 손글씨 판독 오류가 있을 수 있음(설명 {n_cap}/{len(rows)}장). "
        f"생성 {TODAY} · [주차 전체 목록](../README.md) · 전체판 학습자료에는 같은 사진이 촬영 시각 기준으로 해당 슬라이드 위치에 들어 있음.",
        "",
        "| 시각 | 사진 | 판서 내용(AI 설명) |",
        "|---|---|---|",
    ]
    for t, name, cap in rows:
        cap = cap.replace("|", "\\|").replace("\n", " ") if cap else "_(설명 없음)_"
        lines.append(f"| {t[11:] if t else '—'} | [{name}]({name}) | {cap} |")
    (out_dir / "README.md").write_text(scrub_pii("\n".join(lines) + "\n"), encoding="utf-8")
    return {"slug": w["slug"], "n": w["n"], "photos": len(rows), "captions": n_cap, "readme": f"private/docs/{w['slug']}/photos/README.md"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--render-only", action="store_true")
    args = ap.parse_args()
    total = 0
    for w in WEEKS:
        r = process_week(w, args.render_only)
        if r:
            total += r["photos"]
            print(f"{r['slug']}: 사진 {r['photos']}장, 설명 {r['captions']}장 → {r['readme']}")
    print(f"총 {total}장")


if __name__ == "__main__":
    main()
