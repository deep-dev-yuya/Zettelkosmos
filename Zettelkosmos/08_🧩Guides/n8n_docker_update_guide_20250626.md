---
title: "n8n Docker版アップデート手順"
tags: ["n8n", "Docker", "アップデート", "自動化"]
created: 2025-06-26
type: guide
---

## ✅ 概要

このノートでは、Docker を利用してセルフホストしている n8n のアップデート手順をまとめています。以下のステップで **安全に最新版へ更新** できます。

---

## 🔧 アップデート手順

### 1. バックアップ（念のため）

```bash
docker cp n8n-docker-n8n-1:/home/node/.n8n ~/n8n_backup/
```

これは `.n8n` ディレクトリ（設定やデータ）をローカルへバックアップする操作です。

---

### 2. イメージの取得（pull 最新版）

```bash
docker pull n8nio/n8n
```

---

### 3. 一旦停止・再構築

```bash
cd ~/Projects/n8n-docker

docker compose down
docker compose pull
docker compose up -d
```

⚠️ `docker-compose.yml` に `version:` が書かれていると警告が出ますが、現時点では無視してOKです。

---

### 4. バージョン確認（念のため）

```bash
docker exec -it n8n-docker-n8n-1 n8n --version
```

---

## 💡 補足アドバイス

- アップデート前に `~/check_n8n.sh` などで稼働確認しておくと安心です。
- Docker Desktop または `docker login` に失敗することがあるため、ログイン情報はキャッシュしておくか、ログイン不要の pull モードで問題ないかを検証してください。
- `ボリューム永続化` を設定していれば、再構築してもデータが保持されます。

---

## 🔁 Templater での再利用コマンド（例）

```markdown
<% tp.user.insert_update_log("n8n", "Docker によるアップデート", "バージョン1.99.1へ更新") %>
```

---

## 📎 関連リンク

- [n8n公式アップデートガイド](https://docs.n8n.io/hosting/updates/)
- [n8n DockerHubページ](https://hub.docker.com/r/n8nio/n8n)

