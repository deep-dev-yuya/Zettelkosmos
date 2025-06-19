---
title: GitHubプッシュの完全ガイド（初回〜通常運用）
tags: [Git, GitHub, 初心者向け, 操作ガイド]
type: guide
status: published
created: 2025-06-20
updated: 2025-06-20
---

# 🚀 GitHubプッシュの完全ガイド（初回〜通常運用）

このノートは、**GitとGitHubの連携を初めて行う人向け**に、初回セットアップと通常時の操作手順をわかりやすく解説したものです。Zettelkosmosの導入時に実際に遭遇したつまずきポイントも反映しています。

---

## 🧱 事前準備（初回に1度だけ）

| 項目 | 説明 |
|------|------|
| ✅ Gitのインストール | macOSでは標準搭載。なければ`brew install git`などで導入 |
| ✅ GitHubアカウント作成 | https://github.com で作成 |
| ✅ リポジトリ作成（GitHub） | Web上で「新しいリポジトリ」を作成しておく（READMEや.gitignoreは追加しないのが基本） |
| ✅ パーソナルアクセストークン（PAT）発行 | GitHub設定 > Developer Settings > Tokens（repo権限にチェック） |

---

## 🌀 初回のローカル → GitHub連携の流れ（Pushまで）

```bash
# 1. 作業ディレクトリへ移動
cd ~/Documents/Zettelkosmos

# 2. Git初期化
git init

# 3. .gitignore 作成（Obsidianの設定や .DS_Store など除外）
touch .gitignore
# 例：echo ".DS_Store" >> .gitignore

# 4. 最初のファイル追加（README.md なども含む）
git add .

# 5. 初回コミット
git commit -m "初期構成：README, .gitignore, フォルダ作成など"

# 6. リモートリポジトリのURLを登録
git remote add origin https://github.com/ユーザー名/リポジトリ名.git

# 7. GitHubへ初回Push（ユーザー名とPAT入力）
git push -u origin master
```

🧩 **つまずきポイントと対処法**
- 「Operation not permitted」→ macOSのフルディスクアクセス許可を確認（iTermなど）
- 認証失敗 → PAT入力（パスワードでは不可）、必要に応じてKeychain削除
- `.gitignore` などが無視されない → ファイルを追加後、再addしてcommit

---

## 🔁 通常運用時（ノートや設定の更新）

```bash
# 変更があったら add
git add .

# 内容をコミット（メッセージは任意）
git commit -m "ノート追加・設定変更など"

# GitHubへ反映
git push
```

📝 備考：
- commitメッセージは日本語OK
- 画像ファイルやテーマCSSなどもそのまま管理できる
- push後、GitHub上で履歴確認や差分も見える

---

## 🧠 応用Tips
- **indexノートに履歴まとめ**や**更新ログ**を書くと可視化しやすい
- `.gitignore`の設定は定期的に見直し（プラグインやキャッシュ類の除外）
- ターミナル操作に慣れてきたら `alias` で簡略化も可能！

