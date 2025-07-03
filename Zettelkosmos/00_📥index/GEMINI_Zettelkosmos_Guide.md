# GEMINI.md

このVault「Zettelkosmos」は、学習・開発・自動化・情報整理を統合するための**知識管理システム**です。  
構造化されたノート、AIアシスタントとの対話、GitHubによるバージョン管理を組み合わせて運用されています。

---

## 🗂 フォルダ構成と用途

| フォルダ名             | 説明                                |
| ----------------- | --------------------------------- |
| `00_📩index/`     | トップページ、リンク集、MOCノートなどのハブ           |
| `03_🛠Tools/`     | スニペット、ショートカット、ツール設定など技術的メモ        |
| `05_📚Reference/` | 外部情報の整理や参照資料（type: guide）         |
| `06_🧠Notes/`     | 気づき・知見・思考ログなどのナレッジ集積（type: note）  |
| `07_🗃Logs/`      | 日次・週次・学習ログなどの時系列記録（type: log）     |
| `08_🧩Guides/`    | やり方・HowTo・実践ノート（type: guide）      |
| `09_📘Manuals/`   | アプリやツール（例：GitHub、Obsidian）の詳細操作解説 |
| `10_🇹Templates/` | Templater・Dataview 対応テンプレート群      |
| `20_🛠Projects/`  | 実際に進行中のプロジェクト管理                   |
| `90_📦Archive/`   | 使用頻度の低いノート、完了・保管済み内容など            |

---

## 🔧 技術的特徴

- **Dataview** に対応したYAML構造（title / created / type / tags など）
- **Templater** による自動整形テンプレート
- **Minimal Theme + JP Snippet** による視認性の高いUI
- **ChatGPT / Gemini CLI** によるAI対話＋操作補助
- **Git + GitHub連携** による完全ローカル運用＋定期push

---

## 🤖 AIとの連携例

| 使用ツール | 主な活用方法 |
|------------|--------------|
| ChatGPT | ノートの整形・校正・要約、スクリプト生成 |
| Gemini CLI | README生成・ガイド作成・自然言語でのVault操作補助 |
| n8n | 自動通知、ログ記録、LINE連携等の自動化処理 |

---

## ✅ 運用ルール（抜粋）

- ノートはすべてYAMLメタ情報付きでDataview集約対象とする
- テンプレートは `10_Templates/` 配下に配置し、自動整形対応
- フォルダ単位に `_README.md` や `GEMINI.md` の導入を推奨
- 不要ノートはアーカイブ化し、Vault全体の整理性を維持

---

## 🌐 外部連携・今後の拡張

- **GitHub連携**：Zettelkosmos全体の公開も視野に
- **Gemini CLI**：Vault構造を把握した上で、READMEや操作支援を強化
- **Obsidian Publish（検討中）**：外部共有用ページの整備

---

## 📌 ToDo（2025年7月）

- `index.md` の整理とリンク強化
- 各フォルダに `_README.md` または `GEMINI.md` の設置
- `Projects/` に新プロジェクト（例：X翻訳Bot）の追加
- `Manuals/Obsidian` ノートの拡張
