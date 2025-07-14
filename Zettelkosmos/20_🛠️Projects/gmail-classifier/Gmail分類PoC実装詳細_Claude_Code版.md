---
title: Gmail分類PoC実装詳細（Claude Code版）
tags: [プロジェクト, Gmail, PoC, 機械学習, 分類, 実装, Claude Code, Flask, n8n]
created: 2025-07-12
type: project
status: completed
---

# 📌 Gmail分類PoC実装詳細（Claude Code版）

本ドキュメントは、ZETTELKOSMOSの[[Gmail分類PoC手順書_MCP連携版]]をベースに、Claude Codeを活用して`/Users/hasegawayuya/Projects/dev-projects/gmail-classifier/`に完全な実装を行った詳細記録です。

---

## ✅ 実装概要

### 🎯 プロジェクト目的
- Gmail受信メールの自動分類システム構築
- 機械学習（SVM + TF-IDF）による高精度分類
- n8n + Flask + MCP連携によるワークフロー自動化
- LINE通知 + Google Sheets記録による完全自動化

### 🏗 技術アーキテクチャ
```
Gmail API → n8n → Flask API → 機械学習モデル
    ↓         ↓        ↓            ↓
受信監視   前処理   分類・文脈補完   結果出力
    ↓         ↓        ↓            ↓
LINE通知 ← n8n ← API応答 ← 分類結果・信頼度
Google Sheets ← ログ保存 ← 全処理履歴
```

### 🔧 技術スタック詳細
- **Backend**: Flask 2.3.3 + Python 3.10+
- **ML Framework**: scikit-learn 1.3.0 (LinearSVC, TfidfVectorizer)
- **Workflow Engine**: n8n (Docker版)
- **API Integration**: Gmail API, LINE Messaging API, Google Sheets API
- **Infrastructure**: tmux (セッション管理), Docker (n8n), venv (Python環境隔離)

---

## 🗂 プロジェクト構造完全詳細

### 📁 ディレクトリ構成
```
gmail-classifier/
├── app/                           # Flask APIアプリケーション
│   ├── __init__.py               # アプリファクトリー、CORS設定
│   ├── classifier.py             # メール分類API Blueprint
│   └── context_enricher.py       # MCP文脈補完API Blueprint
├── models/                        # 機械学習モデル関連
│   ├── __init__.py              # パッケージ初期化
│   ├── train_model.py           # モデル学習スクリプト
│   └── model.pkl                # 学習済みモデル（実行後生成）
├── n8n/                          # n8nワークフロー定義
│   ├── workflow_sample.json     # 完全なワークフロー定義
│   └── setup_guide.md          # n8nセットアップ手順書
├── data/                         # 学習・テストデータ
│   └── train_data.csv          # サンプル学習データ（15件）
├── tests/                        # 自動テストスイート
│   ├── __init__.py             # テストパッケージ
│   ├── test_api.py             # Flask APIテスト
│   └── test_model.py           # 機械学習モデルテスト
├── scripts/                      # ユーティリティスクリプト
│   └── quick_test.py           # 動作確認スクリプト
├── logs/                         # アプリケーションログ
├── config/                       # 設定ファイル置き場
├── docs/                         # プロジェクトドキュメント
├── config.py                    # Flask設定（開発・本番環境対応）
├── requirements.txt             # Python依存関係定義
├── .env.example                # 環境変数テンプレート
├── run.py                      # メイン実行ファイル
└── README.md                   # プロジェクト説明書
```

---

## 🚀 実装詳細

### 📄 主要ファイル実装内容

#### 1. `run.py` - メイン実行ファイル
```python
#!/usr/bin/env python3
from flask import Flask
from app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
```

**設計思想**: シンプルなエントリーポイント、アプリファクトリーパターン採用

#### 2. `app/__init__.py` - Flask アプリファクトリー
**主要機能**:
- Flask アプリケーション初期化
- CORS 設定（n8nからのクロスオリジンアクセス対応）
- Blueprint 登録（classifier, context_enricher）
- ヘルスチェックエンドポイント提供

#### 3. `app/classifier.py` - メール分類API
**実装機能**:
- `/api/classify` POST エンドポイント
- TF-IDF + SVM による分類実行
- モデルの遅延読み込み（初回アクセス時）
- 信頼度スコア計算
- エラーハンドリング

**API仕様**:
```json
POST /api/classify
{
  "subject": "支払い期限のお知らせ",
  "body": "クレジットカード料金の引き落とし日が近づいています"
}

Response:
{
  "classification": "支払い関係",
  "confidence": 0.85,
  "text_length": 45,
  "model_status": "loaded"
}
```

#### 4. `app/context_enricher.py` - MCP文脈補完API
**実装機能**:
- `/api/enrich-context` POST エンドポイント
- キーワードベース文脈分析
- 期限情報の正規表現抽出
- 優先度レベル判定
- エンティティ抽出（金額、日付、組織）

**分析ロジック**:
- **支払い関係**: 支払い、請求、料金、引き落とし等のキーワード検出
- **会議・スケジュール**: 会議、ミーティング、打ち合わせ等
- **緊急度**: 緊急、至急、重要、urgent等
- **期限抽出**: 正規表現による日付パターンマッチング

#### 5. `models/train_model.py` - 機械学習モデル学習
**実装機能**:
- CSVデータ読み込み（存在しない場合はサンプルデータ生成）
- TF-IDF特徴量抽出（max_features=2000, ngram_range=(1,2)）
- LinearSVC学習
- 学習評価（accuracy, classification_report）
- モデル永続化（pickle形式）

**サンプルデータ**:
- 支払い関係: 5件
- 通知: 5件  
- 重要: 5件
合計15件の多様なメールサンプル

#### 6. `n8n/workflow_sample.json` - n8nワークフロー定義
**ワークフロー構成**:
1. **Gmail Trigger**: IMAP接続、メール監視
2. **Email Preprocessing**: HTMLタグ除去、テキスト正規化
3. **MCP Context Enricher**: 文脈情報抽出（Webhook）
4. **AI Classification**: メール分類実行（Webhook）
5. **Switch分類**: 分類結果による分岐処理
6. **LINE通知**: 重要メール通知
7. **Google Sheets**: 全件ログ保存

---

## 🔧 技術仕様・設計思想

### 🏛 アーキテクチャ設計原則

#### 1. マイクロサービス指向
- Flask API: 分類・文脈補完の独立サービス
- n8n: ワークフローオーケストレーション
- 疎結合設計: 各コンポーネントの独立性確保

#### 2. 拡張性・保守性
- Blueprint による機能分離
- 設定ファイル外部化（config.py, .env）
- 環境別設定対応（開発・本番・テスト）

#### 3. エラーハンドリング・ロバスト性
- API エラーレスポンスの標準化
- モデル読み込み失敗時のフォールバック
- ログ機能による問題追跡

### 🤖 機械学習モデル設計

#### 1. アルゴリズム選択理由
- **SVM (LinearSVC)**: 高次元テキストデータに最適
- **TF-IDF**: 日本語メールの特徴量抽出に適合
- **ngram_range=(1,2)**: 単語・2-gram組み合わせで文脈考慮

#### 2. 特徴量エンジニアリング
- 件名・本文の結合処理
- HTML除去・正規化
- 最大特徴量数制限（計算効率とメモリ使用量のバランス）

#### 3. 評価・改善戦略
- train_test_split による評価
- classification_report による詳細分析
- 継続的な学習データ拡充を想定

### 🔗 API設計思想

#### 1. RESTful設計
- 明確なエンドポイント分離
- HTTP メソッド適切利用
- ステータスコード標準準拠

#### 2. 入力検証・セキュリティ
- 必須フィールド検証
- JSON形式統一
- CORS適切設定

#### 3. レスポンス設計
- 統一的なJSON構造
- エラー情報の詳細化
- デバッグ情報付与

---

## 🧪 テスト・品質保証

### 📊 テストスイート構成

#### 1. `tests/test_api.py` - APIテスト
**テストカバレッジ**:
- ヘルスチェック機能
- メール分類API（正常・異常系）
- 文脈補完API（支払い検出含む）
- モデル状態確認API

#### 2. `tests/test_model.py` - MLモデルテスト
**テストカバレッジ**:
- サンプルデータ生成機能
- モデル学習プロセス
- 分類性能検証

#### 3. `scripts/quick_test.py` - 動作確認スクリプト
**検証項目**:
- サーバー起動状態確認
- 各種分類パターンテスト
- 文脈補完機能テスト
- エラー処理確認

### 🔍 品質保証プロセス
1. **自動テスト**: pytest による回帰テスト
2. **手動テスト**: quick_test.py による統合テスト
3. **コード品質**: Black, flake8 による静的解析準備
4. **API テスト**: cURL コマンドによる外部テスト

---

## 🛠 セットアップ・運用手順

### 🎯 クイックスタート
```bash
# 1. プロジェクトディレクトリ移動
cd /Users/hasegawayuya/Projects/dev-projects/gmail-classifier

# 2. 仮想環境構築
python3 -m venv venv
source venv/bin/activate

# 3. 依存関係インストール
pip install -r requirements.txt

# 4. 環境変数設定
cp .env.example .env
# 必要なAPIキー設定

# 5. モデル学習
cd models && python train_model.py

# 6. サーバー起動
python run.py

# 7. 動作確認
python scripts/quick_test.py
```

### 🔑 必要な環境変数
- `LINE_CHANNEL_ACCESS_TOKEN`: LINE Messaging API
- `GOOGLE_SHEETS_CREDENTIALS_FILE`: Google Sheets API認証
- `GOOGLE_SHEETS_SPREADSHEET_ID`: 保存先スプレッドシート
- `SECRET_KEY`: Flask セッション管理用

### 📡 n8n ワークフロー設定
1. `n8n/workflow_sample.json` をn8nにインポート
2. Gmail API認証設定
3. Webhook URL設定（Flask API連携）
4. LINE、Google Sheets API設定
5. 詳細は `n8n/setup_guide.md` を参照

---

## 🧭 今後の拡張・改善案

### 🚀 短期改善（1-2週間）
- [ ] 学習データ拡充（現在15件→100件以上）
- [ ] 信頼度閾値による人間確認フロー実装
- [ ] ログローテーション機能追加
- [ ] Docker化（Flask API含む）

### 🎯 中期拡張（1-2ヶ月）
- [ ] モデル自動再学習機能
- [ ] リアルタイム分類精度ダッシュボード
- [ ] 多言語対応（英語メール分類）
- [ ] WebUI管理画面実装

### 🌟 長期展望（3-6ヶ月）
- [ ] 深層学習モデル（BERT系）導入
- [ ] クラウドデプロイ（AWS/GCP）
- [ ] 他メールサービス対応（Outlook等）
- [ ] エンタープライズ機能（ユーザー管理、権限制御）

### 🔄 継続的改善
- **データ品質向上**: 分類ミスの継続的フィードバック
- **性能最適化**: レスポンス時間改善、メモリ使用量削減
- **セキュリティ強化**: API認証、暗号化通信
- **監視・アラート**: システム稼働監視、異常検知

---

## 🔗 関連リソース・参照

### 📚 プロジェクト関連ノート
- [[Gmail分類PoC手順書_MCP連携版]] - 元の手順書
- [[Gmail分類PoC補足提案]] - 発展的提案
- [[n8n_docker_task_list]] - n8n Docker構築手順

### 🌐 技術リファレンス
- [Flask公式ドキュメント](https://flask.palletsprojects.com/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [n8n Documentation](https://docs.n8n.io/)
- [LINE Messaging API](https://developers.line.biz/ja/docs/messaging-api/)
- [Google Sheets API](https://developers.google.com/sheets/api)

### 🧰 開発ツール・コマンド
```bash
# 開発用コマンド集
pytest tests/                    # テスト実行
python scripts/quick_test.py     # 動作確認
black app/ models/ tests/        # コードフォーマット
flake8 app/ models/ tests/       # 静的解析
curl -X POST http://localhost:5000/api/classify # API直接テスト
```

### 📈 メトリクス・監視
- **分類精度**: 継続的な精度測定と改善
- **レスポンス時間**: API応答速度最適化
- **エラー率**: 障害検知と改善
- **利用統計**: 分類パターン分析

---

## 📝 実装完了ログ

### ✅ 完了項目（2025-07-12）
- [x] プロジェクト構造設計・作成
- [x] Flask API実装（分類・文脈補完）
- [x] 機械学習モデル学習スクリプト
- [x] n8nワークフロー定義
- [x] テストスイート実装
- [x] 設定ファイル・環境変数管理
- [x] README・ドキュメント整備
- [x] クイックテストスクリプト

### 🔄 次回セッション予定
- [ ] 実際のモデル学習実行
- [ ] Flask APIサーバー起動テスト
- [ ] n8n ワークフロー設定・動作確認
- [ ] LINE API・Google Sheets API連携設定

---

*本実装は Claude Code を活用した効率的なプロジェクト構築の実例として、ZETTELKOSMOS の知識体系に統合されます。継続的な改善と拡張により、実用的なメール分類システムへの発展を目指します。*

---

##  コミットメッセージ案

```
feat: 7/12〜7/15分のgmail-classifier関連ノート・日次ログを追加

- 07_📓Logs/2025-07-12.md：日次ログノートを新規作成
- 20_🛠️Projects/gmail-classifier/Gmail分類PoC補足提案.md：PoC補足・AI活用提案ノートを新規作成
- 20_🛠️Projects/gmail-classifier/Gmail分類PoC仮想環境構築記録.md：仮想環境構築記録ノートを新規作成
- 20_🛠️Projects/gmail-classifier/Gmail分類PoC実装詳細_Claude_Code版.md：Claude Code実装詳細ノートを新規作成
```

---

##  コマンド例（コピペ用）

```bash
# ステージング
git add "07_📓Logs/2025-07-12.md" \
        "20_🛠️Projects/gmail-classifier/Gmail分類PoC補足提案.md" \
        "20_🛠️Projects/gmail-classifier/Gmail分類PoC仮想環境構築記録.md" \
        "20_🛠️Projects/gmail-classifier/Gmail分類PoC実装詳細_Claude_Code版.md"

# コミット
git commit -m "feat: 7/12〜7/15分のgmail-classifier関連ノート・日次ログを追加

- 07_📓Logs/2025-07-12.md：日次ログノートを新規作成
- 20_🛠️Projects/gmail-classifier/Gmail分類PoC補足提案.md：PoC補足・AI活用提案ノートを新規作成
- 20_🛠️Projects/gmail-classifier/Gmail分類PoC仮想環境構築記録.md：仮想環境構築記録ノートを新規作成
- 20_🛠️Projects/gmail-classifier/Gmail分類PoC実装詳細_Claude_Code版.md：Claude Code実装詳細ノートを新規作成
"

# プッシュ（必要に応じて）
git push origin main
```

---

この内容でコミットすれば、該当期間のノート追加・更新が履歴にしっかり残ります！  
他に加えたいファイルや、説明の修正希望があればご指示ください。