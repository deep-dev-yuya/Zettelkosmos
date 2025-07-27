---
title: Gmail分類システム – モデル不一致の根本解決ガイド
created: <% tp.date.now("yyyy-MM-dd") %>
updated: <% tp.date.now("yyyy-MM-dd HH:mm") %>
tags: [gmail-classifier, mlops, troubleshooting, guide]
project: gmail-classifier
version: v1.0.0
status: draft
---

> **目的**  
> 学習時は正しいが API では誤分類する「全部『重要』・confidence<0」問題を、モデル／前処理の完全同期と API 再設計で解決する。

## 🗒 概要
- 原因を三つの典型パターンで整理  
- パイプライン化＋単一 pickle 化で **vectorizer と model の食い違い** を根絶  
- `create_paypay_specialized_features` を **単一モジュール** に集約しコピー＆ペーストを廃止  
- Flask サーバーの **確実なホットリロード** とキャッシュ無効化  
- `LinearSVC` の距離値を **確率化 (CalibratedClassifierCV)** して `confidence` を 0–1 表示  
- CI / ユニットテストで再発を防止  

## 🐞 根本原因の整理
| # | 症状 | 主な原因 | 指標 / ログでの兆候 |
|---|---|---|---|
| 1 | 学習精度は高いが API では全件「重要」 | model と vectorizer のバージョン不一致 | `/model/status` は OK でも `confidence` が極端に低い |
| 2 | 同一入力で enhanced_text_length が違う | `create_paypay_specialized_features` が複数定義 | 学習ログと API ログで文字列長が異なる |
| 3 | `/model/reload` 後も変化なし | Flask プロセスが旧オブジェクトを保持 | `lsof -ti:5000` で PID が残り続けている |

## 🛠 統合ソリューション（実装順）

### 1. モデル＋前処理を Pipeline 化して単一 pkl に保存
```python
from sklearn.pipeline import make_pipeline
import joblib

pipe = make_pipeline(vectorizer, model)  # vectorizer=TfidfVectorizer, model=LinearSVC
joblib.dump(pipe, "models/paypay_specialized_v1.pkl")
```

### 2. 特徴量関数を 1 ファイルに集約
```bash
# model_sync_solution.py に集約
diff -u models/model_sync_solution.py app/classifier.py  # 差分ゼロを確認
find app -name "*.pyc" -delete  # キャッシュ削除
```

### 3. Flask 側のリロード手順
```bash
# ポート開放して完全再起動
lsof -ti:5000 | xargs kill -9
python run.py
```
`ModelManager.reload()` 内では
```python
import importlib, model_sync_solution as mss
importlib.reload(mss)  # 関数定義を最新化
```

### 4. `confidence` の確率化
```python
from sklearn.calibration import CalibratedClassifierCV
svc = LinearSVC(C=2.0, class_weight=...)
model = CalibratedClassifierCV(svc, cv=3)
```

## ✅ 実装チェックリスト
- [ ] `models/paypay_specialized_v1.pkl` が 1 ファイルで ～数 MB  
- [ ] `/model/status` → `hash_match: true`  
- [ ] `curl /api/classify` (PayPay例) → `classification:"支払い関係"`, `confidence≥0.5`  
- [ ] ユニットテスト `assert f(txt)==f(txt)` が PASS  
- [ ] CI: 学習 → save_model → Flask 起動 → /classify テストが成功  

## 🔄 継続改善
1. **データ拡張**: 誤分類メールを自動で収集し次回学習に追加  
2. **バージョニング**: `semver + commit-hash` でモデルを識別  
3. **監視**: `/health` エンドポイントに inference サンプルを追加し外形監視  

## ℹ️ 参考コマンド集
```bash
# 依存パッケージ更新
pip install -U scikit-learn pandas numpy

# メモリ使用量確認
python - <<'PY'
import psutil, json, datetime
print(json.dumps({
  "ts": datetime.datetime.now().isoformat(),
  "mem": psutil.virtual_memory()._asdict()
}, indent=2, ensure_ascii=False))
PY
```

---

### Footnotes
- `LinearSVC.decision_function` は超平面からの **signed 距離** で負値=ターゲット以外  
- Pipeline 化により **vectorizer と model のペアリング事故** を構造的に防止  
