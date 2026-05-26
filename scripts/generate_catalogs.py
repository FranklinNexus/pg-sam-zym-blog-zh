"""Build GitHub-friendly README.md catalogs (no Obsidian wikilinks)."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

SECTIONS = [
    (
        REPO / "paul-graham",
        "Paul Graham（PG）",
        "paulgraham.com",
        "https://paulgraham.com/",
        "PG_*.md",
    ),
    (
        REPO / "sam-altman",
        "Sam Altman",
        "blog.samaltman.com",
        "https://blog.samaltman.com/",
        "Sam_*.md",
    ),
    (
        REPO / "zhang-yiming",
        "张一鸣",
        "公开微博、访谈、演讲整理",
        None,
        "ZYM_*.md",
    ),
]


def article_links(folder: Path, pattern: str) -> list[str]:
    lines: list[str] = []
    for path in sorted(folder.glob(pattern)):
        if path.name in ("README.md", "INDEX.md"):
            continue
        title = path.stem
        if title.startswith("PG_"):
            title = title[3:]
        elif title.startswith("Sam_"):
            title = title[4:]
        elif title.startswith("ZYM_"):
            title = title[4:]
        lines.append(f"- [{title}]({path.name})")
    return lines


def write_author_readme(folder: Path, name: str, source_label: str, source_url: str | None, pattern: str) -> None:
    extra = ""
    if folder.name == "zhang-yiming":
        extra = """

## 参考书单

- [张一鸣推荐书单](张一鸣推荐书单.md)

## 飞书公开整理

见 [`feishu/README.md`](feishu/README.md)
"""
    source_line = f"**原文来源：** [{source_label}]({source_url})" if source_url else f"**材料：** {source_label}"
    articles = article_links(folder, pattern)
    body = f"""# {name} · 中文译文目录

{source_line}

共 **{len(articles)}** 篇。文件名前缀便于区分：`PG_` / `Sam_` / `ZYM_` 仅在本目录内使用。

## 全部篇目

{chr(10).join(articles)}
{extra}
"""
    (folder / "README.md").write_text(body.strip() + "\n", encoding="utf-8")


def write_feishu_readme() -> None:
    folder = REPO / "zhang-yiming" / "feishu"
    if not folder.is_dir():
        return
    lines: list[str] = []
    for path in sorted(folder.glob("FS_*.md")):
        title = path.stem[3:] if path.stem.startswith("FS_") else path.stem
        lines.append(f"- [{title}]({path.name})")
    body = f"""# 张一鸣 · 飞书公开整理

共 **{len(lines)}** 篇。与上级目录的 `ZYM_` 访谈/微博稿分开存放。

## 篇目

{chr(10).join(lines)}
"""
    (folder / "README.md").write_text(body.strip() + "\n", encoding="utf-8")


def main() -> None:
    for folder, name, label, url, pattern in SECTIONS:
        if folder.is_dir():
            write_author_readme(folder, name, label, url, pattern)
    write_feishu_readme()
    print("catalogs written")


if __name__ == "__main__":
    main()
