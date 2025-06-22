---
title: Periodic Notesの使い方
tags: [manual, obsidian, plugin]
type: manual
status: published
created: 2025-06-22
updated: 2025-06-22
---

# 🗓 Periodic Notes の使い方

## ✅ プラグイン概要

「Periodic Notes」は、日次・週次・月次・年次ノートなどの周期的なノートを効率よく管理・生成できるプラグインです。  
テンプレートとの連携や、他プラグイン（Calendar・Templater）と組み合わせて使うことで、時間単位の知識整理を加速させます。

---

## 🔧 推奨初期設定

### 基本ステップ

1. プラグインを有効化
2. 「Settings」→「Periodic Notes」から以下を設定：
   - Daily Notes
   - Weekly Notes
   - Monthly Notes
   - Yearly Notes
3. 各種ノートのテンプレートファイルのパスを指定（※Templater連携）

---

## ⚙️ 主な設定項目と意味

| 設定項目 | 説明 |
|----------|------|
| Folder | ノートが生成されるフォルダ |
| Template | 使用するテンプレートのパス |
| Format | 日付のフォーマット（例: YYYY-MM-DD） |
| Open on startup | Obsidian起動時に自動で開く |

---

## 💡 活用TIPS

- 「Daily Notes」×「Task管理」で、日単位のタスク記録がスムーズに
- 「Weekly Notes」で1週間の振り返りを自動化
- 「Monthly Notes」で月次目標や成果をテンプレートで管理

---

## 🧩 応用例

- **Templater連携**で、ノート生成時に自動的に日付やタスク構造を挿入
- **Dataview**と併用し、全ての周期ノートをテーブル表示で管理

```dataview
table title, file.day
from "07_📓Logs"
where contains(tags, "daily")
```

---

## 🛠 他プラグインとの連携

- **Calendar** → 日次ノートへのリンク・日付選択が容易に
- **Templater** → 自動テンプレ挿入
- **QuickAdd** → タスク入力を素早く

---

## 🔚 まとめ

「定期記録をObsidianで効率化したい」方には必携のプラグインです。  
ログ・レビュー・進捗管理が定着化することで、知識の質も高まります。
