---
tags: [tmux, ターミナル, タイル分割, ワークスペース管理]
aliases: [tmux 基本, ターミナル分割, セッション操作]
created: 2025-07-02
type: guide
---

# tmux の基本と使い方ガイド

## 🧠 概要

このノートは、`tmux` のセッション・ウィンドウ・ペイン管理、および iTerm2 での実践的な活用方法をまとめたガイドです。

---

## 📁 基本構造

| 用語       | 説明                                                                 |
|------------|----------------------------------------------------------------------|
| **セッション** | プロジェクト単位の作業空間。仮想環境や用途で分離可能。例: obsidian, n8n |
| **ウィンドウ** | セッション内のタブのようなもの（通常は1つでOK）                      |
| **ペイン**     | 画面を分割して複数の操作を並行するための領域                         |

---

## 🛠 よく使う操作コマンド

### 🔹 セッション関連

```bash
# 新規セッション作成
tmux new -s セッション名

# セッション一覧
tmux ls

# セッションに接続
tmux attach -t セッション名

# セッション名変更
tmux rename-session -t 旧名 新名

# セッション終了（安全に）
exit

# 他のセッションすべて終了（注意）
tmux kill-session -a
```

### 🔹 ペイン分割（同一セッション内）

```bash
# 横に分割
Ctrl + b → %

# 縦に分割
Ctrl + b → "

# ペイン移動（上下左右）
Ctrl + b → ← / → / ↑ / ↓

# ペインを閉じる
exit
```

---

## 🔄 入力が全ペインに反映されてしまうとき

`synchronize-panes` が ON になっているとき、入力がすべてのペインに反映されます。

### ✔ OFF にするには：

```bash
# 手動で即座にOFF
Ctrl + b → :setw synchronize-panes off

# 永続的にOFF（.tmux.conf）
echo 'set-window-option -g synchronize-panes off' >> ~/.tmux.conf
tmux source-file ~/.tmux.conf
```

---

## 🗂 セッションの分け方（実例）

| セッション名 | 用途                |
|--------------|---------------------|
| obsidian     | Obsidianノート管理   |
| shell        | 通常操作用シェル     |
| n8n          | 自動化・n8n関連作業  |
| Gemini       | Gemini CLIやAI関連   |

---

## ✅ トラブル時のヒント

- **間違えてペインを閉じても**：再分割してもセッションが維持されていれば環境は維持される
- **名前の付け間違い**：`rename-session` でいつでも修正可能
- **同期状態か確認**：
  ```bash
  tmux show-options -w | grep synchronize-panes
  ```

---

## 📎 メモ

- `.tmux.conf` は `~/.tmux.conf` に配置
- iTerm2でも `tmux` によるペイン分割を利用可能
- セッションは「作業プロジェクト単位」で分けると便利

