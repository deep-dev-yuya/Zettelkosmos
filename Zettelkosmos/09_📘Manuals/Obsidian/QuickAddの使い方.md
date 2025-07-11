---
title: QuickAddの使い方
tags: [manual, obsidian, plugin]
type: manual
status: published
created: 2025-06-22
updated: 2025-06-22
---

# 🚀 QuickAdd プラグインの使い方

## 🔍 概要

QuickAddは、Obsidian内で定型的なタスク・テンプレート・ノートの挿入をショートカットやメニューで即実行できる強力なプラグインです。たとえば「今日の作業ログをテンプレートから作成」や「選択肢からノートを分岐生成」など、ルーチンを一発で自動化できます。

## ⚙️ 初期設定とおすすめ構成

1. **コマンドパレットで QuickAdd を検索して起動**
2. `Manage Macros` → `+ Add Macro` でマクロを作成
3. `Choice` を追加して、実行アクションを設定

おすすめ設定例：

- `Template` → `Templater` 経由でテンプレ挿入
- `Capture` → 任意フォルダにログ記録
- `Multi` → 複数アクションを連続実行

## 📌 設定項目の解説

| 設定名              | 意味と活用法                                      |
|--------------------|-----------------------------------------------|
| Choice Name        | メニューに表示される名前                        |
| Type               | アクションの種類（テンプレ挿入・スクリプト実行など） |
| Template Path      | 使用するテンプレートのパス（Templater併用推奨）     |
| Capture Location   | 保存先フォルダ（Daily Logs など）               |
| Hotkey             | キーボードショートカットに割り当て可              |

## 💡 活用提案

- 日記作成、週次レビュー、学習ログテンプレート生成に最適
- スニペット登録＋タグ付けで「ナレッジ登録ボタン」化も可能
- `IF`構文による条件分岐マクロで高度な処理も可能

## 🔗 他プラグインとの連携

- `Templater` と組み合わせることで、変数展開＋ファイル名自動生成などが実現
- `Periodic Notes` に割り込ませて、定時テンプレ作成
