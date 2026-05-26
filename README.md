# Founder Blog 中文译文库

Paul Graham、Sam Altman、张一鸣的**公开博客与访谈**中文译文合集。  
网上零散翻译不少，但**成体系、可检索、尤其张一鸣早期微博/飞书整理**较难找——本仓库用于集中分享，方便阅读与检索。

> 原文均为公开材料；译文仅供学习交流。详见 [NOTICE.md](NOTICE.md)。

## 收录规模

| 目录 | 内容 | 篇数 |
| --- | --- | --- |
| [`paul-graham/`](paul-graham/) | PG 散文（`PG_*.md`） | **231** |
| [`sam-altman/`](sam-altman/) | Sam 博客（`Sam_*.md`） | **59** |
| [`zhang-yiming/`](zhang-yiming/) | 微博手记、访谈、深度稿（`ZYM_*.md`） | **19** |
| [`zhang-yiming/feishu/`](zhang-yiming/feishu/) | 飞书 wiki 整理（`FS_*.md`） | **10** |

各目录下的 **`INDEX.md`** 为 Obsidian 库中的导航页（含分类与链接）。

## 快速入口

- Paul Graham：[如何获得新点子](paul-graham/PG_如何获得新点子.md) · [如何做出伟大的工作](paul-graham/PG_如何做出伟大的工作.md) · [完整目录](paul-graham/INDEX.md)
- Sam Altman：[如何成功](sam-altman/Sam_如何成功.md) · [三点观察](sam-altman/Sam_三点观察.md) · [完整目录](sam-altman/INDEX.md)
- 张一鸣：[微博手记索引](zhang-yiming/ZYM_微博手记索引.md) · [飞书目录](zhang-yiming/feishu/README.md) · [完整目录](zhang-yiming/INDEX.md)

## 单篇格式

每篇文首通常包含：

```markdown
> 原文：<https://...>
> 来源：...
> 英文标题：...（如有）
```

张一鸣飞书整理另含 `> 整理` / `> 对照` 等说明。

## 与 Obsidian 库同步

本地维护的 Obsidian 笔记库更新后，可在本目录运行：

```powershell
python scripts/sync_from_vault.py
```

默认从 `E:\Obsidian Vault\30_Library` 复制 `PG_*`、`Sam_*`、`ZYM_*` 及 `张一鸣_飞书/` 下 markdown。

## 相关项目

同一维护者的 **Agent Skills**（行为蒸馏，非译文）：

- [paul-graham-skills](https://github.com/FranklinNexus/paul-graham-skills)
- [sam-altman-skills](https://github.com/FranklinNexus/sam-altman-skills)
- [zhang-yiming-skills](https://github.com/FranklinNexus/zhang-yiming-skills)

## 许可

- 仓库结构与本仓库译文整理：[MIT](LICENSE)
- 原文版权归各原作者；使用前请阅读 [NOTICE.md](NOTICE.md)
