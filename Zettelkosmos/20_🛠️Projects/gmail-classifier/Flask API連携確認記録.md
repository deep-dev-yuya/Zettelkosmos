---
title: Flask API連携確認記録
tags: [プロジェクト, Gmail, PoC, Flask, API, 連携確認, モデル, Claude Code]
created: 2025-07-16
type: project
status: completed
related: 
  - "[[Gmail分類PoCモデル学習実行記録]]"
  - "[[Gmail分類PoC仮想環境構築記録]]"
  - "[[Gmail分類PoC実装詳細_Claude_Code版]]"
---

# 📌 Flask API連携確認記録

## 🎯 作業概要

Gmail AI Classifier PoCプロジェクトの**Flask APIと新しいmodel.pklの連携確認**を実施した詳細記録です。

**実行日時**: 2025-07-16  
**作業者**: Claude Code  
**目的**: 学習済みモデルとFlask APIエンドポイントの動作確認

---

## 📂 プロジェクト情報

| 項目 | 詳細 |
|------|------|
| **プロジェクト名** | Gmail AI Classifier PoC |
| **プロジェクト場所** | `/Users/[ユーザー名]/Projects/dev-projects/gmail-classifier` |
| **Flask API場所** | `app/` ディレクトリ |
| **モデルファイル** | `models/model.pkl` (7.3KB) |
| **メイン実行ファイル** | `run.py` |

---

## 🔍 Flask API構成確認

### 📁 ファイル構成
```
app/
├── __init__.py          # アプリケーションファクトリー
├── classifier.py        # 分類エンドポイント
└── context_enricher.py  # 文脈補完エンドポイント
```

### 🧩 主要コンポーネント

#### 1. アプリケーションファクトリー (`app/__init__.py`)
```python
def create_app():
    app = Flask(__name__)
    CORS(app)  # n8nからのアクセス用
    
    # Blueprint登録
    app.register_blueprint(classifier_bp, url_prefix='/api')
    app.register_blueprint(context_bp, url_prefix='/api')
    
    @app.route('/health')
    def health_check():
        return {"status": "healthy", "service": "gmail-classifier"}
```

#### 2. 分類エンドポイント (`app/classifier.py`)
```python
def load_model():
    """機械学習モデルの読み込み"""
    global _model, _vectorizer
    
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')
    
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            _vectorizer, _model = pickle.load(f)
    else:
        # デモ用の簡易分類器でフォールバック
```

**主要エンドポイント**:
- `POST /api/classify` - メール分類
- `GET /api/model/status` - モデル状態確認

---

## 🔗 model.pkl連携確認

### 📊 連携仕様

| 項目 | 詳細 |
|------|------|
| **モデルパス** | `../models/model.pkl` (相対パス) |
| **読み込み形式** | pickle (tuple: vectorizer, model) |
| **キャッシュ方式** | グローバル変数 (`_model`, `_vectorizer`) |
| **フォールバック** | ダミーモデル自動生成 |

### 🔧 読み込み処理詳細
```python
# モデルファイル存在確認
model_path = "/Users/[ユーザー名]/Projects/dev-projects/gmail-classifier/app/../models/model.pkl"

# pickle読み込み
with open(model_path, 'rb') as f:
    _vectorizer, _model = pickle.load(f)
    
# グローバルキャッシュで高速化
```

---

## 🚀 API起動テスト

### 1. サーバー起動確認 ✅

**実行コマンド**:
```bash
source /Users/[ユーザー名]/envs/gmail-classifier-env/bin/activate
python -c "from app import create_app; app = create_app(); app.run(host='0.0.0.0', port=5001)"
```

**起動結果**:
```
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5001
* Running on http://192.168.1.9:5001
* Serving Flask app 'app'
* Debug mode: off
```

**注意**: ポート5000はmacOS AirPlay Receiverが使用中のため5001を使用

### 2. ヘルスチェック ✅

**リクエスト**:
```bash
curl -X GET "http://localhost:5001/health"
```

**レスポンス**:
```json
{
  "service": "gmail-classifier",
  "status": "healthy"
}
```

### 3. モデル状態確認 ✅

**リクエスト**:
```bash
curl -X GET "http://localhost:5001/api/model/status"
```

**レスポンス**:
```json
{
  "model_file_exists": true,
  "model_loaded": false,
  "model_path": "/Users/[ユーザー名]/Projects/dev-projects/gmail-classifier/app/../models/model.pkl"
}
```

**結果**: model.pklファイルは存在するが、初回アクセス前のためまだ読み込まれていない状態

---

## 🧪 分類エンドポイント動作テスト

### テスト仕様
- **エンドポイント**: `POST /api/classify`
- **入力形式**: `{"subject": "件名", "body": "本文"}`
- **出力形式**: `{"classification": "分類", "confidence": 信頼度, "model_status": "loaded"}`

### 📋 テストケース実行結果

#### 1. 支払い関係テスト ❌

**入力**:
```json
{
  "subject": "PayPay残高チャージ完了",
  "body": "PayPay残高への料金引き落としが完了しました。"
}
```

**出力**:
```json
{
  "classification": "通知",
  "confidence": -0.14814137733624516,
  "model_status": "loaded",
  "text_length": 40
}
```

**結果**: ❌ **誤分類** (期待: 支払い関係 → 実際: 通知)

#### 2. プロモーションテスト ❌

**入力**:
```json
{
  "subject": "Amazon タイムセール 期間限定",
  "body": "Amazonタイムセールが開催中です。お得な商品をチェックしてください。"
}
```

**出力**:
```json
{
  "classification": "通知",
  "confidence": -0.14814137733624516,
  "model_status": "loaded",
  "text_length": 55
}
```

**結果**: ❌ **誤分類** (期待: プロモーション → 実際: 通知)

#### 3. 重要・緊急テスト ✅

**入力**:
```json
{
  "subject": "緊急 システム障害 サーバーエラー",
  "body": "システムに緊急事態が発生しました。復旧作業を開始します。"
}
```

**出力**:
```json
{
  "classification": "重要",
  "confidence": -0.08050442386851908,
  "model_status": "loaded",
  "text_length": 46
}
```

**結果**: ✅ **正分類** (期待: 重要 → 実際: 重要)

---

## 📊 テスト結果分析

### 🎯 分類精度サマリー

| テストケース | 期待カテゴリ | 実際の分類 | 信頼度 | 結果 |
|-------------|-------------|----------|--------|------|
| PayPay残高チャージ | 支払い関係 | 通知 | -0.148 | ❌ |
| Amazonタイムセール | プロモーション | 通知 | -0.148 | ❌ |
| システム障害 | 重要 | 重要 | -0.081 | ✅ |

**成功率**: 1/3 (33.3%)

### 🔍 発見した問題点

#### 1. モデルバージョン不一致 🚨
- **問題**: APIが読み込んでいるモデルは**旧版（3カテゴリ）**
- **現状**: ['支払い関係', '通知', '重要']
- **期待**: ['支払い関係', 'プロモーション', '重要', '仕事・学習']

#### 2. 学習データ不足 🚨
- **問題**: 基本サンプルデータ（15件）で学習されたモデル
- **影響**: 新しいカテゴリ（プロモーション、仕事・学習）に未対応
- **必要**: 拡張版データ（45件）での再学習

#### 3. 分類精度の問題 🚨
- **問題**: 同一信頼度(-0.148)で「通知」に分類される傾向
- **原因**: 学習データ不足による過学習
- **対策**: データ拡充とハイパーパラメータ調整

---

## 🔧 技術詳細

### Flask API仕様

#### リクエスト形式
```bash
curl -X POST "http://localhost:5001/api/classify" \
-H "Content-Type: application/json" \
-d '{"subject":"件名","body":"本文"}'
```

#### レスポンス形式
```json
{
  "classification": "分類カテゴリ",
  "confidence": 信頼度スコア,
  "model_status": "loaded",
  "text_length": テキスト長
}
```

#### エラーハンドリング
```json
{
  "error": "Missing required fields: subject, body"
}
```

### モデル詳細
- **アルゴリズム**: LinearSVC + TfidfVectorizer
- **特徴量**: 最大2000語、N-gram(1,2)
- **保存形式**: pickle (tuple)
- **サイズ**: 7.3KB

---

## ✅ 正常動作確認項目

### 🟢 成功項目
1. **Flask API起動**: ポート5001で正常起動
2. **ヘルスチェック**: `/health`エンドポイント応答
3. **モデル読み込み**: model.pklファイル正常読み込み
4. **API呼び出し**: JSON形式でのリクエスト・レスポンス
5. **エラーハンドリング**: 不正リクエスト時の適切なエラー応答
6. **信頼度計算**: decision_function()による信頼度算出

### 🔴 改善が必要な項目
1. **モデル更新**: 拡張版4カテゴリモデルへの差し替え
2. **分類精度**: より多くの学習データでの再学習
3. **カテゴリ対応**: 新カテゴリ（プロモーション、仕事・学習）への対応

---

## 🔄 次のステップ

### 📈 優先度高: モデル更新
1. **拡張版モデル学習**: 45件データで4カテゴリモデル生成
2. **model.pkl差し替え**: 新しいモデルでの上書き
3. **API再テスト**: 各カテゴリでの分類精度確認

### 📊 精度向上施策
1. **学習データ拡充**: 各カテゴリ100件以上に増強
2. **前処理改善**: 日本語形態素解析の導入
3. **ハイパーパラメータ調整**: グリッドサーチによる最適化

### 🔗 システム連携
1. **n8nワークフロー連携**: エンドツーエンドテスト
2. **LINE/Google Sheets連携**: 通知・記録機能確認
3. **本格運用準備**: パフォーマンス・セキュリティ対策

---

## 📝 技術メモ

### 使用コマンド履歴
```bash
# Flask API起動
python -c "from app import create_app; app = create_app(); app.run(host='0.0.0.0', port=5001)"

# ヘルスチェック
curl -X GET "http://localhost:5001/health"

# モデル状態確認
curl -X GET "http://localhost:5001/api/model/status"

# 分類テスト
curl -X POST "http://localhost:5001/api/classify" \
-H "Content-Type: application/json" \
-d '{"subject":"テスト件名","body":"テスト本文"}'

# サーバー停止
lsof -ti:5001 | xargs kill -9
```

### 環境情報
- **Python**: 3.13.0
- **仮想環境**: `/Users/[ユーザー名]/envs/gmail-classifier-env`
- **Flask**: 2.3.3
- **scikit-learn**: 1.7.0

---

## 🚨 重要な発見事項

### 現在のモデル状況
- ✅ **ファイル存在**: model.pklは正常に存在
- ✅ **読み込み機能**: pickleからの読み込み成功
- ❌ **モデル内容**: 旧版（3カテゴリ）を使用中
- ❌ **分類精度**: 新カテゴリ未対応

### 解決が必要な課題
1. **モデル差し替え**: 拡張版4カテゴリモデルへの更新
2. **データ品質**: より実用的な学習データの準備
3. **精度向上**: 実用レベルまでの分類精度改善

---

**作成者**: Claude Code  
**最終更新**: 2025-07-16  
**関連ドキュメント**: [[Gmail分類PoCモデル学習実行記録]], [[Gmail分類PoC仮想環境構築記録]]

---

## 🔗 参考リンク

- [Flask API Documentation](https://flask.palletsprojects.com/)
- [scikit-learn Pickle Documentation](https://scikit-learn.org/stable/model_persistence.html)
- プロジェクトリポジトリ: `https://github.com/deep-dev-yuya/gmail-classifier.git`