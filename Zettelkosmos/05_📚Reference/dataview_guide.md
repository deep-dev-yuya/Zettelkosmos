---
title: Dataview クエリ活用ガイド
tags: [obsidian, dataview, reference]
type: reference
status: published
created: 2025-06-21
updated: 2025-06-21
---

## Dataview クエリ活用ガイド

ObsidianのDataviewプラグインを活用するための基本ルールと使用例をまとめました。YAMLメタデータに対応したノート構造を利用し、クエリで自動一覧化や抽出が可能になります。

---

### ✅ クエリ構文の基本

```dataview
table title, tags, status
from "your-folder"
where contains(tags, "obsidian")
sort updated desc
```

- `table`：表形式で出力（他に`list`や`task`も可）
- `from`：対象とするフォルダ名（""必須）
- `where`：条件フィルタ（タグ・ステータス・文字列など）
- `sort`：並び順（`created` / `updated` など）

---

### 📌 表形式の例（titleと更新日）

```dataview
table title, updated
from "reference"
sort updated desc
```

---

### 📋 タスクリストを抽出（未完了のみ）

```dataview
task
from "tasks"
where !completed
```

---

### 📎 特定タグを含むノート一覧

```dataview
list
from "projects"
where contains(tags, "machine-learning")
```

---

### 🛠 よく使う条件構文

| 条件      | 説明例                                 |
|-----------|----------------------------------------|
| `contains(tags, "X")` | タグに「X」が含まれる        |
| `status = "draft"`     | ステータスがdraftのノート    |
| `file.name = "abc"`    | ファイル名がabcと一致        |
| `updated >= date(2024-01-01)` | 更新日が指定日以降     |

---

### 🧠 メモ

- `from` は必ず "フォルダ名" の形式で指定。
- YAMLにフィールド（例：title, tags, type, status, created, updated）が正しく書かれていないと抽出できません。
- `dataviewjs` を使うとJavaScriptによる柔軟な出力も可能（上級者向け）。

---
