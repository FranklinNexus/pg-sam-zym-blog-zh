"""Copy PG / Sam / ZYM translation markdown from Obsidian vault into this repo."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

VAULT_LIB = Path(r"E:\Obsidian Vault\30_Library")
REPO = Path(__file__).resolve().parents[1]

PG_OUT = REPO / "paul-graham"
SAM_OUT = REPO / "sam-altman"
ZYM_OUT = REPO / "zhang-yiming"
ZYM_FEISHU = ZYM_OUT / "feishu"

HUB_COPIES = [
    (VAULT_LIB / "Paul Graham.md", PG_OUT / "INDEX.md"),
    (VAULT_LIB / "Sam Altman.md", SAM_OUT / "INDEX.md"),
    (VAULT_LIB / "张一鸣.md", ZYM_OUT / "INDEX.md"),
    (VAULT_LIB / "张一鸣_飞书.md", ZYM_FEISHU / "INDEX.md"),
    (VAULT_LIB / "张一鸣_飞书" / "README.md", ZYM_FEISHU / "README.md"),
]


def copy_glob(pattern: str, dest: Path) -> list[Path]:
    dest.mkdir(parents=True, exist_ok=True)
    copied: list[Path] = []
    for src in sorted(VAULT_LIB.glob(pattern)):
        if not src.is_file() or src.suffix.lower() != ".md":
            continue
        if ".sync-conflict" in src.name:
            continue
        target = dest / src.name
        shutil.copy2(src, target)
        copied.append(target)
    return copied


def main() -> None:
    pg = copy_glob("PG_*.md", PG_OUT)
    sam = copy_glob("Sam_*.md", SAM_OUT)
    zym = copy_glob("ZYM_*.md", ZYM_OUT)

    feishu_src = VAULT_LIB / "张一鸣_飞书"
    feishu: list[Path] = []
    if feishu_src.is_dir():
        ZYM_FEISHU.mkdir(parents=True, exist_ok=True)
        for src in sorted(feishu_src.glob("*.md")):
            if ".sync-conflict" in src.name:
                continue
            target = ZYM_FEISHU / src.name
            shutil.copy2(src, target)
            feishu.append(target)

    for src, dst in HUB_COPIES:
        if src.is_file():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    print(f"paul-graham: {len(pg)} articles")
    print(f"sam-altman: {len(sam)} articles")
    print(f"zhang-yiming: {len(zym)} articles + {len(feishu)} feishu")
    print(f"total markdown: {len(pg) + len(sam) + len(zym) + len(feishu) + sum(1 for s, _ in HUB_COPIES if s.is_file())}")


if __name__ == "__main__":
    main()
