# 维护者说明

从 Obsidian 同步并生成 GitHub 目录：

```powershell
python scripts/sync_from_vault.py
```

- 正文来自 `E:\Obsidian Vault\30_Library`
- 不复制 Obsidian 的 `INDEX.md`（含 `[[wikilink]]`，在 GitHub 上无效）
- 同步后自动生成各目录下的 `README.md` 篇目列表

提交建议：

```powershell
python C:\Users\kfr34\Desktop\Program\git_commit_clean.py . "Sync from vault"
git push
```
