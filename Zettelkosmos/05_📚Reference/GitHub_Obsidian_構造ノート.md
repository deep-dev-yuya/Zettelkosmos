---
title: GitHub初期プッシュとObsidian構造の対応関係
tags: [Git, GitHub, Obsidian, 初期構築]
type: guide
status: published
created: 2025-06-20
updated: 2025-06-20
---

# GitHub初期プッシュとObsidian構造の対応関係

## 🌱 初回プッシュとは？
- GitHubの初回Pushでは、プロジェクトの**基本構造（外枠）**を固める。
- Obsidianでいうと `.obsidian/` や `README.md`、`.gitignore` などの設定類が中心。

## 🧱 Obsidianの構造にたとえると

| 区分 | 内容 | Gitでのタイミング |
|------|------|------------------|
| 外枠 | UIテーマ、フォルダ構成、README、.gitignore | 初回プッシュ |
| 内枠 | ノート内容（.md）、タグ、リンク、MOC構成など | 日々の更新ごとにコミット＆プッシュ |

## 📂 初回に含まれる代表ファイル
- `.obsidian/appearance.json`
- `.obsidian/plugins/`
- `README.md`
- `.gitignore`
- 空のフォルダ（`.keep` などで管理）

## 🔄 今後の更新時
- ノートの追加・編集：新規コミットで保存
- 設定変更：必要に応じてコミット（例：テーマ変更）

## 💡 ワンポイント
- GitHubは「構造のバックアップ＋変更履歴の記録」として非常に有効。
