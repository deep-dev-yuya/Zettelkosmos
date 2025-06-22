---
title: Style Settingsの使い方
tags: [manual, obsidian, plugin]
type: manual
status: published
created: 2025-06-22
updated: 2025-06-22
---

# 🎨 Style Settings プラグインの使い方

## 🧾 概要

Style Settings は、テーマやCSSスニペットで定義されたスタイル項目をGUIで簡単に変更・適用できるプラグインです。MinimalテーマやITSテーマとの併用で、視認性・可読性を大幅に向上できます。

## ⚙️ 初期設定とおすすめ構成

1. テーマ側にStyle設定があるか確認（例：Minimal）
2. 設定 → Style Settings を開いて各項目を調整
3. スニペット側に設定項目があると自動で読み込まれる

## 📌 主な設定項目例（Minimalテーマ）

| 設定名                       | 意味とおすすめ設定                           |
|----------------------------|------------------------------------------|
| Headings Size              | 見出しサイズを調整（1.2〜1.5推奨）            |
| Custom Accent Color        | 強調色（リンクや強調マーカーに反映）         |
| Scrollbar Visibility       | スクロールバーの表示／非表示                 |
| Code Block Style           | コードブロックの背景・枠線                   |
| Line Width                 | 本文の最大幅（読みやすさ向上に重要）         |

## 💡 活用提案

- カラーユニバーサル対応：アクセント色の調整で可視性改善
- コードブロックのカスタマイズで開発ノートの見やすさUP
- DataviewテーブルやCalloutに合わせた装飾の最適化

## 🛠 スニペット活用との併用

Style Settings は `.css` スニペットにも対応しており、以下のような形で拡張できます：

```css
body {
  --h1-size: 2.2em;
  --callout-radius: 12px;
}
```
