---
title: Dataviewクエリのサンプル
tags: [Dataview, クエリ, サンプル]
type: guide
status: published
created: 2025-06-20
updated: 2025-06-20
---

# Dataviewクエリの基本サンプル

以下は、Dataviewプラグインを使ってノートの一覧を表示する基本的なクエリの例です。

---

## 📋 最新のノート5件を表示

```dataview
table title, created
sort created desc
limit 5
```

---

## 🔖 特定タグ（#ショートカット）付きノートを一覧表示

```dataview
table title, tags, created
where contains(tags, "ショートカット")
sort created desc
```

---

## 📂 特定フォルダ（"Shortcuts"）内のノート一覧

```dataview
list
from "Shortcuts"
sort file.name asc
```

---

## ✅ チェックボックス付きタスク一覧（未完了）

```dataview
task
where !completed
```

---

このノートはDataviewのクエリ文法を学ぶための基本テンプレートとしてご利用いただけます。
