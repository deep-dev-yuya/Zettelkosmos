---
title: GitHubへの日々のプッシュ手順
created: 2025-06-25
tags: [GitHub, プッシュ手順, Obsidian対応]
type: guide
---

# GitHubへの日々のプッシュ手順（解説付き）

## ✅ 基本操作の流れ

```bash
git add .
git commit -m "fix: ログノートを追加（2025-06-25）"
git push origin main
```

- `git add .`：すべての変更をステージング
- `git commit -m "..."`：変更内容に応じて適切なメッセージを記述
- `git push`：GitHubへ反映

---

## 📝 推奨 commit メッセージ prefix 一覧

| prefix | 用途例 |
|--------|--------|
| feat:  | 新機能の追加 |
| fix:   | バグ修正 |
| docs:  | ドキュメントのみの変更 |
| style: | フォーマット修正（意味のない変更） |
| refactor: | リファクタリング |
| chore: | その他の雑務的変更（依存更新など） |

---

## 🔧 commit メッセージ例（日報向け）

- `docs: 2025-06-25の日報を追加`
- `chore: タグと整理用の補足コメントを追加`
- `fix: 変数名の誤記を修正`

---

## 💡 Obsidian Vaultでの管理に向けて

このノートはObsidianでの知識管理にも利用できます。日々の操作やルールを記録し、再発防止やスムーズな習慣化に役立てましょう。

