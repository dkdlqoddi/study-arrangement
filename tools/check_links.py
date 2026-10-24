#!/usr/bin/env python3
"""
저장소 안 Markdown 문서의 상대 링크가 실제 파일을 가리키는지, 파일이 토큰 한도를 넘지 않는지 점검.

    python3 tools/check_links.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {"machine_learning_for_health_science", ".git", "node_modules", ".venv"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def md_files():
    for p in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        yield p


def main() -> int:
    broken = []
    nlinks = 0
    for p in md_files():
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in LINK_RE.finditer(text):
            target = m.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#")[0]
            if not target:
                continue
            nlinks += 1
            dest = (p.parent / target).resolve()
            if not dest.exists():
                broken.append((str(p.relative_to(ROOT)), target))
    print(f"상대 링크 {nlinks}개 점검, 깨진 링크 {len(broken)}개")
    for src, t in broken:
        print(f"  {src} -> {t}")

    manifest = ROOT / "private" / "manifest.json"
    if not manifest.exists():
        manifest = ROOT / "docs" / "manifest.json"
    if manifest.exists():
        m = json.loads(manifest.read_text(encoding="utf-8"))
        limit = m.get("max_tokens", 12000)
        files = [f for w in m.get("weeks", []) for e in w["entries"] for f in e["files"]]
        files += [f for e in m.get("compiled", []) for f in e["files"]]
        files += [f for e in m.get("common", []) for f in e["files"]]
        # 공개 문서(docs/)가 비공개 경로(private/)를 가리키면 안 됨
        leaks = []
        for p in ROOT.joinpath("docs").rglob("*.md"):
            for mm in LINK_RE.finditer(p.read_text(encoding="utf-8", errors="replace")):
                dest = (p.parent / mm.group(1).split("#")[0]).resolve() if not mm.group(1).startswith(("http", "#", "mailto")) else None
                if dest and "private" in dest.relative_to(ROOT).parts[:1]:
                    leaks.append((str(p.relative_to(ROOT)), mm.group(1)))
        for root_md in ("README.md", "INDEX.md", "TOPICS.md", "llms.txt"):
            q = ROOT / root_md
            if q.exists():
                for mm in LINK_RE.finditer(q.read_text(encoding="utf-8", errors="replace")):
                    t = mm.group(1)
                    if t.startswith("private/") or "/private/" in t:
                        leaks.append((root_md, t))
        print(f"공개 문서에서 비공개 경로를 가리키는 링크 {len(leaks)}개")
        for src, t in leaks:
            print(f"  {src} -> {t}")
        over = [f for f in files if f["tokens"] > limit]
        missing = [f["path"] for f in files if not (ROOT / f["path"]).exists()]
        print(f"manifest 문서 {len(files)}개, 한도({limit:,} tokens) 초과 {len(over)}개, 누락 {len(missing)}개")
        for f in over:
            print(f"  초과: {f['path']} {f['tokens']:,}")
        for f in missing:
            print(f"  누락: {f}")
        return 1 if (broken or over or missing or leaks) else 0
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
