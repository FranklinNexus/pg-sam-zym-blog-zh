"""Copy PG / Sam / ZYM translation markdown from Obsidian vault into this repo."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

VAULT_LIB = Path(r"E:\Obsidian Vault\30_Library")
REPO = Path(__file__).resolve().parents[1]

PG_OUT = REPO / "paul-graham"
SAM_OUT = REPO / "sam-altman"
ZYM_OUT = REPO / "zhang-yiming"
ZYM_FEISHU = ZYM_OUT / "feishu"
READING_LIST_OUT = ZYM_OUT / "张一鸣推荐书单.md"


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


def remove_obsidian_hubs() -> None:
    for path in [
        PG_OUT / "INDEX.md",
        SAM_OUT / "INDEX.md",
        ZYM_OUT / "INDEX.md",
        ZYM_FEISHU / "INDEX.md",
    ]:
        if path.is_file():
            path.unlink()


def main() -> None:
    pg = copy_glob("PG_*.md", PG_OUT)
    sam = copy_glob("Sam_*.md", SAM_OUT)
    zym = copy_glob("ZYM_*.md", ZYM_OUT)

    feishu: list[Path] = []
    feishu_src = VAULT_LIB / "张一鸣_飞书"
    if feishu_src.is_dir():
        ZYM_FEISHU.mkdir(parents=True, exist_ok=True)
        for src in sorted(feishu_src.glob("*.md")):
            if ".sync-conflict" in src.name or src.name == "README.md":
                continue
            target = ZYM_FEISHU / src.name
            shutil.copy2(src, target)
            feishu.append(target)

    remove_obsidian_hubs()
    subprocess.run([sys.executable, str(REPO / "scripts" / "generate_catalogs.py")], check=True)

    extra = 1 if READING_LIST_OUT.is_file() else 0
    print(f"paul-graham: {len(pg)}")
    print(f"sam-altman: {len(sam)}")
    print(f"zhang-yiming: {len(zym)} + feishu {len(feishu)} + reading-list {extra}")


if __name__ == "__main__":
    main()
