---
title: Obsidian視認性強化スニペット（最強版CSS付き）
tags: [obsidian, css, snippet, customization]
type: guide
status: published
created: 2025-06-21
updated: 2025-06-21
---

## ✅ 概要

このノートでは、Obsidianの視認性と装飾性を高める「最強CSSスニペット」の内容と、その使い方についてまとめています。

---

## 🎨 主なカスタマイズ内容

### 1. コードブロック装飾（通常・インライン対応）
- `.markdown-rendered code` や `.markdown-preview-view pre` にスタイル適用
- フォント変更・背景色調整・角丸・パディング追加

### 2. Dataview出力強化
- 表・リスト・コード含むDataview表示を装飾
- 可読性を向上し、背景色と境界を強調

### 3. Calloutのカスタム装飾とアニメーション
- `callout[data-callout="ai"]`, `"tip"`, `"warning"` などに専用アイコン・背景
- `@keyframes` でアニメーション（点滅・ゆらゆら・回転など）

### 4. ノート全体の視認性向上
- 箇条書き、リンク、引用、タイトルの強調

---

## 🛠 CSSスニペット（zettel-style.css）

```css
/* === コードブロック（全体）=== */
.markdown-rendered pre code,
.markdown-preview-view pre code {
  background-color: #2e3440;
  color: #d8dee9;
  border-radius: 10px;
  padding: 1em;
  font-family: 'Fira Code', monospace;
}

/* === インラインコード === */
.markdown-rendered code {
  background-color: #3b4252;
  padding: 0.2em 0.4em;
  border-radius: 4px;
  color: #88c0d0;
}

/* === Dataview表 === */
.dataview.table-view-table {
  background-color: #1f1f1f;
  border: 1px solid #444;
  border-radius: 8px;
}
.dataview.table-view-table th,
.dataview.table-view-table td {
  padding: 8px;
  border: 1px solid #333;
}

/* === カスタムCallout === */
.callout[data-callout="ai"] {
  background: linear-gradient(135deg, #232526 0%, #414345 100%);
  border-left: 4px solid #88c0d0;
}
.callout[data-callout="ai"] .callout-icon svg {
  animation: pulse-ai 2s infinite;
}

.callout[data-callout="tip"] {
  background: #2e8b57;
  border-left: 4px solid #98fb98;
}
.callout[data-callout="tip"] .callout-icon svg {
  animation: spin-tip 5s linear infinite;
}

@keyframes pulse-ai {
  0% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.1); opacity: 0.7; }
  100% { transform: scale(1); opacity: 1; }
}

@keyframes spin-tip {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

---

## 🔁 運用方法（再現手順）

1. 上記CSSを `zettel-style.css` という名前で保存
2. Obsidianの `.obsidian/snippets` フォルダへ配置
3. Obsidianの設定 → 外観 → スニペットから有効化
4. テーマとの競合を避けるために最後に読み込むようにする（ファイル名に `zz_` を付けるなど）

---

## ✅ 備考・今後の追加候補

- チェックリスト・タグの視認性強化
- Mermaid（図式）の装飾追加
- コードブロックに言語名ラベル追加
- プラグインごとのカスタム対応（Excalidrawなど）

---
このノートは再利用可能なテンプレートとして保管できます。
