# 发布到 GitHub

## 1. 在 GitHub 新建空仓库

建议名称：`founder-blog-zh`（或你喜欢的名字，勿勾选 README / .gitignore）。

## 2. 关联远程并推送

```powershell
cd C:\Users\kfr34\Desktop\Program\founder-blog-zh

git remote add origin https://github.com/FranklinNexus/founder-blog-zh.git
git push -u origin main
```

若远程名或仓库名不同，替换 URL 即可。

## 3. 日后从 Obsidian 更新

```powershell
python scripts/sync_from_vault.py
git add -A
git commit -m "Sync translations from vault"
git push
```

> 若 Cursor 自动在 commit 里加 `Co-authored-by: Cursor`，可用  
> `python C:\Users\kfr34\Desktop\Program\git_commit_clean.py . "你的说明"`  
> 在仓库根目录执行（把 `.` 换成本仓库路径）。
