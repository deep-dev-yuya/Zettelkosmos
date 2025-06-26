---
title: n8n Dockerアップデート手順と運用ノート
created: 2025-06-26
tags: [n8n, docker, アップデート, ガイド, obsidian]
type: guide
---

# 🐳 n8n Dockerアップデートガイド

これは、ローカル永続化された n8n コンテナのアップデート作業を再現できるようにまとめた手順と補足ノートです。

---

## ✅ 目的

- `n8n` のDockerイメージを最新化し、既存の永続化データを維持したままコンテナを再構築する。

---

## 🔧 アップデート手順（コマンド付き）

```bash
# 1. n8n コンテナを停止（必要に応じて）
docker stop n8n-docker-n8n-1

# 2. 現在のデータをバックアップ（任意）
docker cp n8n-docker-n8n-1:/home/node/.n8n ~/n8n_backup/

# 3. 最新のn8nイメージを取得
docker pull n8nio/n8n

# 4. dockerディレクトリに移動
cd ~/Projects/n8n-docker

# 5. コンテナとネットワークを削除
docker compose down

# 6. 念のため再度イメージの取得
docker compose pull

# 7. 再度コンテナをバックグラウンドで起動
docker compose up -d

# 8. 起動確認
docker ps
~/check_n8n.sh   # ← 独自スクリプトで確認するのもOK
```

---

## 💡 補足と注意点

- `docker-compose.yml` に `version:` 属性が含まれていると警告されるため、削除推奨（compose v2では不要）。
- `~/check_n8n.sh` のようなスクリプトがあると、常駐確認が容易になる。
- n8nは **`.n8n` ディレクトリをマウントしている限り、データは保持される**。
- スクリーンセーバー活用や、画面ロックでMacを保護しても n8n は動作可能。

---

## 📌 今後の提案

- `.env` ファイルを導入して環境変数管理を簡素化
- `cron` や `launchctl` を使って定期バックアップを自動化
- 複数のn8nプロジェクトを管理したい場合は、リポジトリやdocker-composeを分ける
- ホスティング移行を視野に入れる場合はRAMやVolume要件を要確認

---

## 📁 関連ファイル・構成（例）

```
n8n-docker/
├── docker-compose.yml
├── .env（あれば）
└── check_n8n.sh（あれば）
```

---

このノートは Obsidian の `90_📦Archive/` フォルダに一時的に配置しておくと管理しやすいです。
