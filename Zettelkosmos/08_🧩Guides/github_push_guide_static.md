---
title: GitHubへの日々のプッシュ手順
tags: [GitHub, プッシュ手順, Obsidian対応]
type: guide
status: draft
created: 2025-07-08
updated: 2025-07-08
---


---

# GitHubへの日々のプッシュ手順（解説付き）

## ✅ 基本操作の流れ

```shell
git add .
git commit -m "コミットメッセージ"
git push origin main
```

- `git add .`：作業ディレクトリ内のすべての変更をステージング（準備状態）にするコマンド
- `git commit -m "..."`：ステージングされた変更に対し説明付きで確定する（履歴に残す）
- `git push origin main`：ローカルの確定済み変更をGitHubのmainブランチへ送信

---

## 📝 推奨 commit メッセージ prefix 一覧

| prefix   | 用途例                                  |
|----------|------------------------------------------|
| feat:    | 新機能の追加                             |
| fix:     | バグ修正                                 |
| docs:    | ドキュメントのみの変更                   |
| style:   | フォーマット修正（意味のない変更）       |
| refactor:| リファクタリング                         |
| chore:   | その他の雑務的変更（依存更新など）       |
| test:    | テストコードの追加・修正                 |

---

## 🛠 commit メッセージ例（日報向け）

- `docs: 2025-07-08の日報を追加`
- `chore: タグと整理用の補足コメントを追加`
- `fix: 変数名の誤記を修正`

---

## 💡 Obsidian Vaultでの管理に向けて

このノートはObsidianでの知識管理にも利用できます。
日々の操作やルールを記録し、再発防止やスムーズな習慣化に役立てましょう。
