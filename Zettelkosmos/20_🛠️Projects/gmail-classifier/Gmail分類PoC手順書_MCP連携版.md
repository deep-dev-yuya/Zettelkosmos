---
title: Gmailメール分類PoC手順書（MCP連携版）
tags: [プロジェクト, Gmail, n8n, MCP, Flask, PoC]
created: 2025-07-08
type: project
status: ongoing
---


# 📌 Gmailメール分類PoC手順書（MCP連携版）

本ドキュメントは、Gmailから受信したメールを機械学習で分類し、n8n＋Flask＋MCPを活用して自動処理するプロジェクトのセットアップ手順をまとめたものです。

---

## ✅ フェーズ1：準備・環境構築

### 🔧 必要ツールの確認
- [x] n8n（Docker運用）
- [x] Python 3.10+（venv推奨）
- [x] tmux（セッション常駐用）
- [ ] Google Sheets API認証
- [ ] LINE Messaging API トークン発行
- [x] GitHubでプロジェクト管理

---

## ✅ フェーズ2：Flask APIサーバー構築

### 🗂 ディレクトリ構成
```bash
gmail-classifier/
├── venv/
├── app/
│   ├── __init__.py
│   ├── context_enricher.py
│   ├── classifier.py
│   ├── model.pkl
└── run.py
```

### 🚀 初期セットアップ
- [x] 仮想環境の作成
- [x] Flask・scikit-learn・pandasのインストール
- [x] run.pyにBlueprint統合

---

## ✅ フェーズ3：n8nワークフロー構築（Claude設計）

### 🔁 メインノード構成
- [x] Gmail Trigger（IMAP）
- [x] Email Preprocessing（HTML除去・正規化）
- [ ] MCP Context Enricherノード（Webhook）
- [ ] AI Classificationノード（Webhook）
- [ ] Switch分類（重要・支払い・通知）
- [ ] LINE通知（Messaging API）
- [ ] Google Sheetsログ保存

---

## ✅ フェーズ4：分類モデルの準備（CSV → モデル学習）

### 📄 CSV形式例
```csv
subject,body,label
"支払い期限のお知らせ","〇〇サービスの料金が〇月〇日に引き落とされます","支払い関係"
"会議のご案内","以下の日程で会議を予定しています","通知"
```

### 🤖 モデル構築（Python例）
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import pandas as pd, pickle

df = pd.read_csv("train_data.csv")
X = df["subject"] + " " + df["body"]
y = df["label"]

vectorizer = TfidfVectorizer(max_features=2000)
X_vec = vectorizer.fit_transform(X)

model = LinearSVC()
model.fit(X_vec, y)

with open("model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)
```
- [ ] CSV作成
- [ ] 学習スクリプト作成
- [ ] model.pkl出力確認

---

## ✅ フェーズ5：MCP文脈補完（Flask側）

### 💡 enrich-contextエンドポイント例
```python
@context_blueprint.route("/enrich-context", methods=["POST"])
def enrich():
    data = request.json
    body = data.get("body", "")
    context = "支払いに関する文脈あり" if "請求" in body else "特別な文脈なし"
    return jsonify({
        "enriched_context": context,
        "context_summary": context,
        "deadline_info": "2025-07-15" if "期限" in body else None
    })
```
- [ ] context_enricher.py 実装
- [ ] Flaskでエンドポイントテスト
- [ ] n8nからPOSTできるか確認

---

## 🧭 今後の展望

- [ ] 信頼度の低い分類を別処理に分岐
- [ ] Google Sheetsログ記録の最適化
- [ ] モデルの再学習フロー（再分類学習）

---

## 🔗 関連リソース

- [ ] LINE Messaging API Docs
- [ ] Google Sheets API Quickstart
- [ ] MCP（Model Context Protocol）仕様メモ（別ノート）
