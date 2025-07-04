---
title: ターミナル基本ルールまとめ
tags: [terminal, command, beginner, guide]
type: guide
status: published
created: 2025-06-30
updated: 2025-06-30
---

## ✅ 概要

このノートでは、ターミナル操作における基本的なルールや用語（スペース、大文字・小文字、引用符、引数など）について、初心者にもわかりやすくまとめています。

---

## 🔟 ターミナル基本ルール10箇条

1. **スペースは半角で**  
   → コマンドと引数の区切りは半角スペースです。全角は無効。

2. **記号も正確に入力する**  
   → ハイフン（`-`）、ドット（`.`）など、**全て半角**で記述。

3. **大文字と小文字は区別される**  
   → `File.txt` と `file.txt` は別ファイルとして扱われます。

4. **ファイル名やフォルダ名は正確に**  
   → スペースを含む場合は引用符 `" "` で囲むと安全です。

5. **引用符を使うと便利**  
   → `"My Folder"` や `'My File.txt'` のように使えます。

6. **コマンドは基本的に小文字**  
   → 例：`git add .`、`ls -la` など。

7. **パスは絶対パス or 相対パスで指定**  
   → `~/Documents` や `../myfolder` のように。

8. **`.`（ドット）はカレントディレクトリ**  
   → `git add .` は「現在のディレクトリすべてを追加」という意味。

9. **引数はコマンドの動作を制御する**  
   → 例：`ls -a` は「隠しファイルも表示」。

10. **実行前に確認・Tab補完を使うと安心**  
   → 長いファイル名やコマンドは `Tab` で補完が可能。

---

## 📝 引用符とは？

引用符とは、文字列を囲むために使う記号のことで、シェルやプログラミング言語で重要な意味を持ちます。

| 種類 | 記号 | 用途 |
|------|------|------|
| ダブルクオーテーション | `" "` | 文字列を囲む。中で変数展開が可能。 |
| シングルクオーテーション | `' '` | 文字列を囲む。中で変数展開しない。 |
| バッククオート（古い形式） | `` `command` `` | コマンドを実行して結果を取得。 |

※ 日本語では「**いんようふ（引用符）**」と呼ばれます。

---

