---
title: Markdown構文・再現ノート（記法＋注意点付き）
tags: [markdown, guide, obsidian]
type: guide
status: published
created: 2025-06-21
updated: 2025-06-21
---

# ✍️ Markdown構文・再現ノート（記法＋注意点付き）

このノートは、Obsidianで自分自身が生成されたノートを**自力で再現・修正・追記**できるようになるための構文ガイドです。  
特に、**小文字/大文字、半角/全角、空白の有無**などでつまずきやすいポイントを明示しています。

---

## ✅ チェックリスト（タスク）

### 構文：
```
- [ ] やること
- [x] 完了したこと
```

### 注意点：
- `-`（ハイフン）は **半角**で書くこと！
- `[ ]` や `[x]` の間には **半角スペース**が必要！
- `[x]` の `x` は **必ず小文字**（`[X]` は無効）

---

## 🔢 見出し（Heading）

```
# 見出し1
## 見出し2
### 見出し3
```

- `#` は **半角**
- `#` と見出し文の間に **半角スペース**が必要（`#見出し` はNG）

---

## 🔗 リンク（Obsidianリンク／外部リンク）

```
[[ノート名]]  ← Vault内リンク
[Google](https://www.google.com) ← 外部リンク
```

- `[[ ]]` は **半角の角括弧×2**
- 外部リンクは `[表示名](URL)` 順で記述（全角括弧不可）

---

## 💬 引用（補足）

```
> これは補足です
```

- `>` は **半角の不等号**
- 後に **半角スペース**が必要（`>補足` はNG）

---

## 📌 箇条書き／番号付きリスト

```
- 箇条書き1
- 箇条書き2

1. 番号1
2. 番号2
```

- `-` や `1.` の後ろに **半角スペース**を忘れずに

---

## 💻 コードブロック（インライン／ブロック）

### インラインコード：
```
`コード`
```

### コードブロック：
````markdown
```python
print("Hello World")
```
````

- バッククォート（ `` ` `` ）は **すべて半角**・3つで囲む
- 言語指定は **小文字英語（例：python, bash）**

---

## 📄 YAMLメタデータ（Dataview用）

```
---
title: ノートタイトル
tags: [tag1, tag2]
type: note
status: draft
created: 2025-06-21
updated: 2025-06-21
---
```

- `---` は **半角のハイフン3つ**
- コロン `:` の後には **半角スペース**
- 配列は `[tag1, tag2]` のように **カンマと半角スペース**

---

## 🔍 よくあるミス一覧表

| 要素 | 正しい | よくある間違い |
|------|--------|----------------|
| チェックリスト | `- [x]` | `- [X]`, `- [ x ]` |
| 見出し | `# タイトル` | `#タイトル`, `＃ タイトル` |
| 引用 | `> 注釈` | `＞注釈`, `>注釈` |
| コード | `` `code` `` | `‘code’`, `“code”`（全角） |
| YAML | `---` で囲む | `ーーー`, `－－－`（全角） |

---

## 🧠 Obsidianでの操作アドバイス

- **Live Preview（ライブ表示）** では意図せぬ変換が起きる場合あり → `Cmd+E` で Sourceモードと切替確認
- Markdownは**シンプルな構文の精度**が命。**見た目が似ていても動作しないことがある**！

---

## 🏁 補足

このノートは `08_Guides/` に格納し、必要に応じて随時更新します。  
「記法をミスしない自信」と「ノート修正への安心感」を得るための1枚です📘

# タイトル
