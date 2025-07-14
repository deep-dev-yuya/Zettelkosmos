---
title: Gmail分類PoC仮想環境構築記録
tags: [プロジェクト, Gmail, PoC, 仮想環境, Python, Claude Code, 環境構築]
created: 2025-07-13
type: project
status: completed
related: 
  - "[[Gmail分類PoC実装詳細_Claude_Code版]]"
  - "[[Gmail分類PoC手順書_MCP連携版]]"
---

# 📌 Gmail分類PoC仮想環境構築記録

## 🎯 作業概要

Gmail AI Classifier PoCプロジェクトの**Python仮想環境構築**を、書類フォルダの「仮想環境環境構築.txt」に従って実行した詳細記録です。

**実行日時**: 2025-07-13  
**作業者**: Claude Code  
**参照文書**: `/Users/hasegawayuya/Documents/仮想環境環境構築.txt`

---

## 📂 プロジェクト情報

| 項目 | 詳細 |
|------|------|
| **プロジェクト名** | Gmail AI Classifier PoC |
| **プロジェクト場所** | `/Users/hasegawayuya/Projects/dev-projects/gmail-classifier` |
| **仮想環境場所** | `/Users/hasegawayuya/envs/gmail-classifier-env` |
| **技術スタック** | Flask + scikit-learn + n8n + MCP連携 |
| **Python版** | Python 3.13.0 |

---

## 🚀 実行タスク詳細

### 1. 仮想環境作成・設定 ✅

```bash
# 仮想環境作成（既存のenvsフォルダーに統一）
python3 -m venv /Users/hasegawayuya/envs/gmail-classifier-env

# 仮想環境有効化
source /Users/hasegawayuya/envs/gmail-classifier-env/bin/activate

# pip更新 (24.2 → 25.1.1)
pip install --upgrade pip
```

**結果**: ✅ Python 3.13.0環境で正常作成

### 2. 依存関係インストール ✅

#### 📋 段階的インストール実行

```bash
# 1. Flask関連パッケージ
pip install Flask==2.3.3 Flask-CORS==4.0.0

# 2. 機械学習ライブラリ（互換性対応）
pip install scikit-learn pandas numpy
# 注意: scikit-learn==1.3.0は Python 3.13で互換性問題のため最新版(1.7.0)使用

# 3. 自然言語処理・ユーティリティ
pip install nltk==3.8.1 requests==2.31.0 python-dotenv==1.0.0

# 4. Google API群
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

# 5. LINE SDK（最新版対応）
pip install line-bot-sdk
# 注意: 3.5.0→3.17.1に自動更新

# 6. 開発・テストツール
pip install pytest==7.4.2 pytest-flask==1.2.0 black==23.7.0 flake8==6.0.0
```

#### 🔧 互換性対応処理

| 元パッケージ | 予定版 | 実際版 | 理由 |
|-------------|--------|--------|------|
| scikit-learn | 1.3.0 | 1.7.0 | Python 3.13 Cython互換性 |
| line-bot-sdk | 3.5.0 | 3.17.1 | 依存関係の最新化 |
| requests | 2.31.0 | 2.32.4 | line-bot-sdkによる要求 |

### 3. 環境確認・テスト ✅

```bash
# Python環境確認
which python  # /Users/hasegawayuya/envs/gmail-classifier-env/bin/python
python --version  # Python 3.13.0
echo $VIRTUAL_ENV  # /Users/hasegawayuya/envs/gmail-classifier-env

# 主要ライブラリ確認
python -c "import flask, sklearn, pandas, numpy; print('✅ All core libraries imported successfully')"
# ✅ All core libraries imported successfully

# Flask動作確認
python -c "from flask import Flask; app = Flask(__name__); print('✅ Flask app creation successful')"
# ✅ Flask app creation successful

# scikit-learn動作確認
python -c "from sklearn.feature_extraction.text import TfidfVectorizer; from sklearn.svm import LinearSVC; print('✅ ML libraries working')"
# ✅ ML libraries working
```

---

## 📦 最終インストール状況

### 🎯 主要パッケージ一覧

| カテゴリ | パッケージ | バージョン | 用途 |
|---------|-----------|-----------|------|
| **Web Framework** | Flask | 2.3.3 | APIサーバー |
| | Flask-CORS | 4.0.0 | CORS対応 |
| **機械学習** | scikit-learn | 1.7.0 | SVM分類器 |
| | pandas | 2.3.1 | データ処理 |
| | numpy | 2.3.1 | 数値計算 |
| **自然言語処理** | nltk | 3.8.1 | テキスト前処理 |
| **Google APIs** | google-api-python-client | 2.176.0 | Gmail/Sheets API |
| | google-auth | 2.40.3 | OAuth2認証 |
| **LINE API** | line-bot-sdk | 3.17.1 | LINE Messaging |
| **開発ツール** | pytest | 7.4.2 | テストフレームワーク |
| | black | 23.7.0 | コードフォーマッタ |
| | flake8 | 6.0.0 | Linter |

### 📊 総インストール数: **67パッケージ**

---

## ✅ 完了確認チェックリスト

- [x] ✅ 仮想環境が`/Users/hasegawayuya/envs/gmail-classifier-env`に作成されている
- [x] ✅ 仮想環境が正常に有効化できる
- [x] ✅ requirements.txtの全依存関係がエラーなくインストール済み
- [x] ✅ Python環境と主要ライブラリ（Flask, scikit-learn）が正常動作
- [x] ✅ 仮想環境パスが正しく設定されている

---

## 🚨 発生した問題と対応

### 問題1: scikit-learn 1.3.0 コンパイルエラー

**エラー**: Python 3.13でCython コンパイルが失敗
```
Cython.Compiler.Errors.CompileError: sklearn/linear_model/_cd_fast.pyx
```

**対応**: 最新版scikit-learn 1.7.0に変更してインストール成功

### 問題2: aiohttp ビルドエラー

**エラー**: line-bot-sdk依存のaiohttp 3.8.5がPython 3.13でビルド失敗

**対応**: line-bot-sdkを最新版3.17.1に更新し、aiohttp 3.12.14で解決

---

## 🔄 次のステップ

仮想環境構築完了後の予定タスク：

1. **Git リポジトリ初期化**（別タスク）
2. **環境変数設定**（.env ファイル作成）
3. **Flask API サーバー起動テスト**
4. **n8nワークフロー連携テスト**

---

## 📝 技術メモ

### Python 3.13 対応状況
- ✅ Flask ecosystem: 完全対応
- ✅ scikit-learn: 1.7.0で対応
- ✅ Google APIs: 完全対応
- ✅ LINE SDK: 最新版で対応

### 仮想環境管理
```bash
# 今後の有効化コマンド
source /Users/hasegawayuya/envs/gmail-classifier-env/bin/activate

# パッケージ確認
pip list

# 環境情報
python --version && echo $VIRTUAL_ENV
```

---

**作成者**: Claude Code  
**最終更新**: 2025-07-13  
**関連ドキュメント**: [[Gmail分類PoC実装詳細_Claude_Code版]], [[Gmail分類PoC手順書_MCP連携版]]