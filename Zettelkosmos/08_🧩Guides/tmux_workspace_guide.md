---
title: tmux ワークスペース管理ガイド
tags: [tmux, ターミナル, タイル分割, ワークスペース管理]
aliases: [tmux 基本, ターミナル分割, セッション操作]
created: 2025-07-02
type: guide
---

# tmux ワークスペース管理ガイド

tmuxを使って、ターミナルの作業スペースを柔軟に管理する方法についてまとめています。

## 🧩 基本構造

tmuxの構造は以下の3階層で成り立っています：

- **セッション（session）**：プロジェクト単位のようなまとまり。
- **ウィンドウ（window）**：セッション内の1画面単位（タブのようなもの）。
- **ペイン（pane）**：ウィンドウ内を分割して表示するターミナル領域。

## 📦 現在の構成例（2025年7月現在）

| セッション名 | 用途               | 備考                     |
|--------------|--------------------|--------------------------|
| obsidian     | Obsidian用         | Zettelkosmosディレクトリ |
| n8n          | n8n自動化関連      | encoding-envを使用       |
| shell        | 通常操作・コマンド |                          |
| gemini       | Gemini CLI         | AIとの対話ターミナル     |

## 🔧 操作コマンド

### ✅ セッション関連

```bash
# 新規セッション開始
tmux new-session -s session_name

# セッション一覧表示
tmux ls

# セッション切り替え
tmux attach-session -t session_name

# セッション名の変更
tmux rename-session -t old_name new_name
```

### ✅ ペイン操作

```bash
# 垂直分割（上下）
tmux split-window -v

# 水平分割（左右）
tmux split-window -h

# ペイン間移動（Ctrl+bを押してから矢印キー）
```

### ✅ ペイン表示状態の確認

```bash
tmux display-message -p "#S"   # 現在のセッション名表示
```

## 🐍 仮想環境操作

```bash
# 仮想環境の有効化（例：python-basics-env）
cd ~/envs/python-basics-env
source bin/activate

# 仮想環境の無効化
deactivate
```

## 📝 Tips

- ペインを閉じてもセッションを終了しない限り他のペインは保持されます。
- 同一セッション内でのペインは通常のタイル分割として機能します。
- それぞれのセッションに名前をつけることで役割が明確になります。

---

このノートは Dataview と Templater に対応しており、日々の作業記録や環境構築の参考にご活用ください。
