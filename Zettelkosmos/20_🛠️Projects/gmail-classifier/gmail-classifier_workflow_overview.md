---
title: Gmail分類ワークフロー構成一覧
created: 2025-07-22
tags: [n8n, gmail, workflow, 構成図, 分類]
type: project
---

# Gmail分類ワークフロー構成（n8n）

n8nで構築されたGmail分類Botのワークフロー構成要素を一覧化。

## 📌 ワークフローノード構成と役割

| ノード名 | 種類 | 役割 |
|---------|------|------|
| Gmail Trigger | Gmail Trigger | Gmail受信トリガー（新着メール検出） |
| Email Preprocessing | Code (JavaScript) | 件名・本文抽出＋受信時刻の統一（internalDateベース） |
| Context Enricher | Webhook (POST) | 高度な文脈情報をFlask API経由で付与 |
| Merge Email + Context | Merge | 上記2つの情報を統合（Combine） |
| Extract Email Summary | Code | メタ情報整理（messageId, subjectなど） |
| AI Classification | HTTP Request (POST) | Flask上のMLモデルで分類処理 |
| Append AI Output to Metadata | Code | 分類結果（分類ラベル・信頼度など）を結合 |
| Merge Metadata + AI Output | Merge | 前処理と分類結果を統合 |
| Route by Classification Label | Switch | 分類ラベルに応じて分岐（支払い・通知・重要など） |
| 各AIラベルノード（6種） | Gmail Label | Gmail上に該当ラベルを付与 |
| Collect All Label Routes | Merge (append) | 全ルートの結果を収束しログ用に集約 |
| Build Log Entry (Final) | Code | スプレッドシート記録用の構造に整形 |
| Google Sheets Log | Google Sheets | 処理結果ログの記録（分類・信頼度・理由） |
| Generate Reason Tag | Code | 信頼度に応じた判定理由付与（要確認/信頼不足など） |

## 🧩 特記事項

- すべての分類がログされるよう、MergeノードとSwitch構成が工夫されている。
- internalDate による正確な受信時刻と日本時間表示に対応済み。
- Claude Codeによりモデル精度とログ設計が強化された。
- Obsidian上でのプロジェクト管理に対応（このファイル含む）。

---

※このファイルは ChatGPT により自動生成されました。
