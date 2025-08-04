---
title: Gmail分類PoC .gitignore定義
tags: [project, gitignore, security]
created: 2025-07-14
project: gmail-classifier
---

# 📄 Gmail分類PoC用 .gitignore 記録

このファイルは、Gmail AI分類PoCプロジェクトにおける `.gitignore` の定義とその意味付けを記録したものです。

## ✅ 目的
- 仮想環境、キャッシュ、機密情報などの **Gitへの誤コミットを防ぐ**
- セキュリティや構成整理の観点から**除外すべきファイル群を体系的に明示**

## 🧠 生成元
Claudeに依頼して生成した内容を元に検証・整理し、最終採用版として記録。

## 📝 内容

```gitignore
# Gmail分類PoC用 .gitignore
# プロジェクト: /Users/[ユーザー名]/Projects/python-basics/gmail-classifier

# ===== Python関連 =====
__pycache__/
*.py[cod]
*$py.class

# 配布物 / パッケージング
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# ユニットテスト / カバレッジレポート
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# ===== 機械学習関連 =====
models/model.pkl
models/*.pkl
models/*.joblib
models/*.h5
models/*.pt
models/*.pth
data/emails/
data/train_data.csv
data/raw_emails/
data/personal_emails/
*.csv
*.xlsx
*.xls

# Jupyter Notebook
.ipynb_checkpoints

# ===== Flask関連 =====
instance/
flask_session/

# ===== 環境変数・認証情報 =====
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
credentials.json
token.json
client_secret.json
service-account-key.json
line_channel_secret.txt
line_access_token.txt
gmail_credentials.json
gmail_token.pickle

# ===== ログファイル =====
logs/
*.log
*.log.*
app.log
error.log
access.log

# ===== n8n関連 =====
.n8n/
n8n-data/

# ===== OS関連 =====
.DS_Store
.AppleDouble
.LSOverride
._*
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent
*~
Thumbs.db
Thumbs.db:encryptable
ehthumbs.db
ehthumbs_vista.db
*.stackdump
[Dd]esktop.ini
$RECYCLE.BIN/
*.cab
*.msi
*.msix
*.msm
*.msp
*.lnk

# ===== エディタ関連 =====
.vscode/
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
!.vscode/*.code-snippets
.idea/
*.swp
*.swo
*.swp
*.swo
*~
\#*\#
.\#*

# ===== 仮想環境 =====
venv/
env/
ENV/
.venv/

# ===== 一時ファイル・キャッシュ =====
*.tmp
*.temp
*.bak
*.backup
*.old

# ===== プロジェクト固有 =====
test_emails/
sample_emails/
reports/
analysis/
*.html
*.pdf
config_local.py
local_settings.py
performance_logs/
benchmark_results/
output/
results/

# ===== セキュリティ重要項目 =====
*secret*
*password*
*private*
*key*
*token*
*.pem
*.p12
*.pfx
```
