---
title: Templaterの使い方
tags: [manual, obsidian, plugin]
type: manual
status: published
created: 2025-06-22
updated: 2025-06-22
---

# 🧩 Templater プラグインの使い方

## 📌 概要

TemplaterはObsidianのテンプレート機能を拡張し、JavaScriptや変数などを使った高度なテンプレート処理を可能にします。定型文の自動化・繰り返し作業の短縮に最適です。

## ⚙️ 初期設定

1. プラグインを有効化後、設定でテンプレートフォルダを指定
2. `Templater User Scripts` を保存するフォルダも任意で設定
3. コマンドパレットまたは他プラグインからテンプレートを呼び出し

## 🔧 設定項目（例）

| 項目名                          | 説明                                        |
|-------------------------------|-------------------------------------------|
| Template folder location      | テンプレートを保存するフォルダ              |
| User Scripts folder location  | JSスクリプトを保存する場所                  |
| Timeout                       | スクリプト実行のタイムアウト時間             |
| Trigger Templater on new file | 新規ファイル作成時に自動テンプレート実行     |

## 🧠 活用アイデア

- 日付付きノートタイトルの自動生成
- カスタム関数によるデータ計算や引用展開
- `QuickAdd` や `Periodic Notes` と組み合わせて定期テンプレ管理

## 💡 よく使う構文例

```md
<% tp.date.now("YYYY-MM-DD") %>
<%*
let project = "プロジェクト名";
tR += `#tag/${project}`
%>
```

## 🛠 応用Tips

- `tp.file.title` や `tp.frontmatter` でファイルメタデータを操作
- JSに習熟すればリッチな自動生成が可能に
