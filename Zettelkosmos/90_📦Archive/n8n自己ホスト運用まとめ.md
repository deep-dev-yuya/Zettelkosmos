---
title: n8n自己ホスト運用まとめ
tags: ['n8n', 'Docker', 'PyCharm', 'Obsidian連携', '自動化', '運用管理']
created: 2025-06-23
type: guide
---


# 🧾 n8n自己ホスト運用まとめ：Docker＋Mac管理＋PyCharm環境

## ✅ 1. 自己ホストn8nの基本確認
- Docker Desktop上にて `n8n-docker` コンテナを起動中。
- コンテナ名：`n8n-docker`
- ステータス確認スクリプト：`~/check_n8n.sh` を使用し `n8n is running` を確認
- Docker Desktopを閉じても常駐確認済み（バックグラウンドで稼働）

## 🔐 2. Macのロックとモニター管理
- セキュリティのために **ホットコーナーでロック** を使用
- ディスプレイスリープ、モニター電源OFFともにDocker/n8n動作は継続
- ロック後のチェックには `check_n8n.sh` スクリプトが有効

## 🧠 3. 開発・確認環境
- ターミナルでDockerログ確認：`docker ps | grep n8n`
- PyCharmにて自動補完とファイル構成を確認（現在も起動中）
- スプリットビュー調整：iTerm2のタイル機能を使用（四分割→下2つ統合も対応）

## 🌐 4. ブラウザとn8n画面
- `http://localhost:5678/` にてn8nへアクセス
- クラウド版には存在しない **「スター表示」** がUI右上にあり
- コンソールでは一部リソースエラーあり（翻訳リクエストなど外部接続）

## 📝 5. その他メモ
- Dockerログイン試行時、過去アカウントに関する警告あり（無視可）
- DevToolsで表示される一部404エラーは自己ホスト版n8n特有のもので影響軽微
- LINE通知連携や永続化設定については今後拡張予定

---

最後にこのノートは Dataview と Templater に対応しており、Zettelkosmos Vault の `90_📦Archive/` に保管されています。
