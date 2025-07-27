---
title: Claude CodeへのGmail分類Workflow修正依頼
created: <% tp.date.now("yyyy-MM-dd") %>
updated: <% tp.date.now("yyyy-MM-dd HH:mm") %>
tags: [n8n, gmail-classifier, claude, workflow-request, ai-collaboration]
project: gmail-classifier
status: draft
executed_by: user
---

## 🎯 依頼目的

Gmailで受信したメールをAI分類し、その分類結果に応じて **Gmailへ自動でラベルを付与**するn8nワークフローへの改修をClaude Codeに依頼する。

## 🧩 背景と現状

- 既存のPoCワークフロー（Claude Code作成済）では以下構成となっている：

```
Gmail Trigger
  ↓
Email Preprocessing
  ↓
MCP Context Enricher
  ↓
Flask APIによる分類
  ↓
Switch（分類ラベルによる分岐）
  ├─ LINE通知（→今回削除対象）
  └─ Google Sheetsログ保存
```

- 現状は分類後にLINE通知を行っているが、**通知処理は別Workflowに完全に分離済み**のため、今回のWorkflowでは **Gmailラベル振り分けに専念**したい。

---

## ✅ 依頼項目（Claude Code向けプロンプト）

```text
目的：Gmailに届いたメールを分類し、Gmail自体にラベルを自動で付与するn8nワークフローを完成させたいです。

現在の構成：
- Claude Code が作成したワークフローがあり、以下の流れで構成されています。
  - Gmail Trigger → Email Preprocessing → MCP Context Enricher → AI Classification（Flask API）→ Switch分岐
  - その後、LINE通知とGoogle Sheets保存に分岐しています。

課題・変更点：
- LINE通知はすでに別のワークフローで運用しているため、ここでは Gmailへのラベル付与を行いたいです。
- Gmail Trigger で取得できる `messageId` を使って、分類されたラベル（例：「支払い関係」「重要」など）を Gmail に付与してください。
- ラベルが存在しない場合は自動作成してもOKです。

要望：
1. 修正済みの n8n ワークフロー構成をわかりやすい図解かステップ一覧で提示
2. Gmailノードでの設定内容（例：Modify Message / Add Label）を記述
3. Switchの条件式例も含めて明記（classificationによる分岐）
4. ラベル名と分類結果を map で一元管理する形にしてもOK
5. Google Sheetsへのログ記録は残す（ラベル・分類・信頼度など）
6. Flask APIエンドポイント：http://localhost:5000/api/classify
7. Gmail modifyスコープ：許可済み
8. オプション：confidence < 0.5 などのケースを「再学習候補」として記録
9. 可能であればn8n JSONワークフローとして出力、または構成図の添付を希望
10. Obsidian用にmd化しやすい出力構成が望ましい（後で整理予定）

よろしくお願いします。
```

---

## 📎 今後の用途

この依頼ノートは Claude Code に提示するプロンプトの保存用であり、  
後日 Obsidian Vault「Zettelkosmos」内のプロジェクトノート群にリンクされる予定。

