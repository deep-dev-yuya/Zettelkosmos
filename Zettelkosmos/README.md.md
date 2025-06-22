---
title: Zettelkosmos Vault README
tags: [vault, overview, guide]
type: guide
status: published
created: 2025-06-21
updated: 2025-06-21
---

# 📘 Zettelkosmos

これは Obsidian を使って構築された、個人のナレッジベース  
（Zettelkasten + Cosmos）です。

---

## 🗂️ Vault概要

- **Vault名**：Zettelkosmos  
- **保存場所**：`~/Documents/Zettelkosmos/`  
- **主な用途**：学習メモ、日々の記録、テンプレート、タグ運用、知識のリンク構築

---

## 🧠 思想背景

Zettelkasten手法に基づいた階層とリンクによる思考支援を目的としています。  
特定のアプリや構造に縛られず、「整理しすぎない整理」がモットーです。

---

## 📁 フォルダ構成ガイド（Zettelkosmos）

このVaultでは、以下のような分類方針でノートを整理しています。

```
00_🏠index/              ← トップページ・MOC系
03_🛠Tools/              ← スニペットや環境構築
05_📚Reference/          ← 外部知識や操作手順（type: guide）
06_🧠Notes/              ← 日々の学びや気づき（type: note）
07_📓Logs/               ← デイリー・週次・学習ログ（type: log）
08_🧩Guides/             ← 実践ガイド・やり方ノート（type: guide）
10_🇹Templates/          ← Templater/Dataviewテンプレ
20_🛠Projects/           ← プロジェクト単位の進行管理（type: project）
90_📦Archive/            ← 使わなくなったノート類
README.md               ← このVaultの使い方・概要
```

> 📌 既存ノートは移動せず、今後の新規作成分からこの構成に基づいて整理・運用していきます。

---

## 🔧 運用ルール概要

- ノート作成時には `YAML` メタデータを含める（Dataviewで活用）
- `type`, `status`, `tags` を適切に記述し分類
- プロジェクトは `20_Projects/`、ガイドは `08_Guides/` に整理
- 簡易的なメモや一時的なものは `Inbox` に保存し、あとで整理
- 構造が複雑になりすぎないよう、**フラットでリンク中心の運用**を優先

---

## 🗓️ 更新履歴

- **2025-06-21**：Vault構成方針を反映した完全版READMEを作成・適用

