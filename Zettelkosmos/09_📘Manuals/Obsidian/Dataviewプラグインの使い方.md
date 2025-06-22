---
title: Dataviewプラグインの使い方
tags: [manual, obsidian, plugin]
type: manual
status: published
created: 2025-06-22
updated: 2025-06-22
---

# 📊 Dataviewプラグインの使い方

## 概要
DataviewはObsidianのメタデータを利用して、ノートをクエリ・フィルタ・並び替えなどが可能な「データベース風」に扱える強力なプラグインです。

## 主な構文
```
table title, status
from "06_🧠Notes"
where type = "note"
sort file.ctime desc
```

## よく使う出力形式
- `table`: 表形式でデータを表示
- `list`: 箇条書きで表示
- `task`: チェックボックス付きのタスクリスト表示

## 設定項目と意味（基本的に設定UIはなし）
Dataviewは設定画面は存在しませんが、YAML構造と構文理解が重要です。

## 活用例
- 学習ログを時系列で並べる
- タグ別に分類されたノートの一覧を生成
- 進行中のプロジェクト一覧を「status」フィールドで絞り込み表示

## 応用TIPS
- `status != "done"` を使って未完了のタスクだけを表示
- `file.link` を使うとクリックで直接ノートを開けるリンクに
- `contains(tags, "AI")` で特定タグを持つノートの抽出

## 注意点
- YAMLメタデータの書き忘れによりクエリに表示されない場合がある
- インデントのミスや構文エラーに注意
