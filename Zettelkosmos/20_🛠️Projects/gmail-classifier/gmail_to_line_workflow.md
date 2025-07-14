---
title: Gmail → LINE通知ワークフロー
tags: [n8n, LINE, Gmail, workflow, project]
created: 2025-07-04
type: project
status: active
---

# 📬 Gmail → LINE通知ワークフロー

n8nで構築したGmail → LINE通知の自動化ワークフロー。文字化け修正を含めた実用的なフィルター通知設計。

---

## 🧩 ノード一覧と処理内容

| ノード名 | 種別 | 処理内容 |
|---------|------|-----------|
| Gmail Watcher (IMAP) | トリガー | Gmailアカウントから新着メールを監視。IMAP経由で取得。 |
| Fix Encoding | Function | メール本文のエンコード状況をチェックし、base64形式の可能性を判定。エンコード情報をフラグとして付与。 |
| If | 条件分岐 | 文字化け（base64）があるかどうかで分岐。true → 修復、false → 通常処理。 |
| HTTP Request | 外部Webhook | FlaskサーバーにPOSTして、base64の本文をUTF-8にデコード。 |
| Format Decoded Body | Function | 修復された本文データから余分なヘッダーなどを削除して整形。 |
| Format LINE Message | Function | 件名・差出人・受信日時・本文（修正後）をLINE用にフォーマット。 |
| Email Filter | Function | 件名・差出人・本文のキーワードで通知対象の絞り込み。スパムや不要通知を除外。 |
| LINE Message Builder | Function | 件名・差出人・受信日時・本文（通常）をLINE用にフォーマット。 |
| Send to LINE | HTTP Request | LINE Messaging APIへメッセージを送信。アクセストークンは環境変数で管理。 |

---

## 🔮 今後の展開案

- ✅ LINE通知の文字数上限チェック機能の追加（エラー回避）
- ✅ ログ保存処理（送信記録／エラー記録）
- ✅ Obsidian日報やZettelkosmosへの自動保存連携
- 🔄 メールの既読化や削除の自動処理
- 📊 通知件数の可視化／週次レポート化

---

## 📝 メモ

- 使用サービス：Gmail（IMAP）, Flask (Fix Encoding API), LINE Messaging API
- テーマ：実用性 × エラー耐性を重視した通知処理
- 備考：tmuxにてFlaskサーバー常駐、n8nはDockerで永続化運用

---

