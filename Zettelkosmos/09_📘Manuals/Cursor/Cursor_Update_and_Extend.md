---
title: Cursor アップデート・拡張方法
tags: [cursor, update, extend, guide]
created: 2025-07-09
updated: 2025-07-09
---

# 🖱️ Cursor アップデート・拡張方法

## 概要
Cursorのアップデート方法と拡張機能の追加・管理について詳しく解説します。最新機能を活用し、カスタマイズして効率的な開発環境を構築しましょう。

## 1. アップデート方法

### 自動アップデートの設定
**手順：**
1. **設定の確認**
   - Settings → Application → Auto Update
   - 自動アップデートを有効化

2. **アップデート通知の設定**
   - アップデート通知を有効化
   - ベータ版の参加設定

3. **アップデートの確認**
   - Help → Check for Updates
   - 最新版の確認

### 手動アップデート
**手順：**
1. **現在のバージョン確認**
   - Help → About Cursor
   - 現在のバージョンを確認

2. **最新版のダウンロード**
   - [公式サイト](https://cursor.sh/)から最新版をダウンロード
   - インストーラーを実行

3. **アップデート後の確認**
   - 設定の確認
   - 拡張機能の動作確認
   - データの整合性確認

### アップデート時の注意点
**事前準備：**
- 重要なファイルのバックアップ
- 設定ファイルのエクスポート
- 拡張機能リストの保存

**アップデート後：**
- 新機能の確認
- 設定の再確認
- 互換性の問題がないか確認

## 2. 拡張機能の管理

### 推奨拡張機能
**開発効率向上：**
- **Auto Rename Tag**: HTMLタグの自動リネーム
- **Bracket Pair Colorizer**: 括弧の色分け
- **GitLens**: Git履歴の詳細表示
- **Live Server**: ローカルサーバーの起動

**AI・自動化：**
- **GitHub Copilot**: AIコード補完
- **Tabnine**: AIコード補完
- **Code Spell Checker**: スペルチェック

**Markdown・文書：**
- **Markdown All in One**: Markdown機能強化
- **Markdown Preview Enhanced**: プレビュー機能
- **Paste Image**: 画像の貼り付け

### 拡張機能のインストール
**手順：**
1. **拡張機能の検索**
   - Extensions → 検索ボックスで拡張機能名を入力
   - カテゴリ別の検索

2. **インストール**
   - 拡張機能の詳細を確認
   - Install ボタンをクリック

3. **設定**
   - 拡張機能の設定を確認
   - 必要に応じて設定を調整

### 拡張機能の管理
**有効/無効の切り替え：**
- Extensions → 拡張機能を選択
- Enable/Disable で切り替え

**設定の変更：**
- Settings → Extensions
- 各拡張機能の設定を調整

**アンインストール：**
- 不要な拡張機能を削除
- 設定ファイルも削除

## 3. カスタマイズ方法

### テーマ・外観のカスタマイズ
**テーマの変更：**
1. **テーマの選択**
   - Settings → Color Theme
   - ダーク/ライトテーマの選択

2. **カスタムテーマの作成**
   - 既存テーマをベースにカスタマイズ
   - 色設定の調整

3. **アイコンテーマ**
   - File Icon Theme の変更
   - ファイルタイプ別のアイコン設定

### キーボードショートカットのカスタマイズ
**ショートカットの変更：**
1. **設定画面を開く**
   - Settings → Keyboard Shortcuts
   - または Cmd+K, Cmd+S

2. **ショートカットの検索**
   - コマンド名で検索
   - カテゴリ別の検索

3. **ショートカットの変更**
   - 既存のショートカットを変更
   - 新しいショートカットを追加

**よく使うカスタムショートカット：**
- ファイルの新規作成
- 特定のフォルダを開く
- よく使うコマンドの実行

### 設定ファイルのカスタマイズ
**settings.json の編集：**
```json
{
  "editor.fontSize": 14,
  "editor.fontFamily": "Fira Code",
  "editor.tabSize": 2,
  "editor.wordWrap": "on",
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000
}
```

**keybindings.json の編集：**
```json
[
  {
    "key": "cmd+shift+r",
    "command": "workbench.action.reloadWindow"
  }
]
```

## 4. 高度なカスタマイズ

### スニペットの作成
**スニペットの作成手順：**
1. **スニペットファイルの作成**
   - File → Preferences → Configure User Snippets
   - 言語を選択

2. **スニペットの定義**
```json
{
  "Console log": {
    "prefix": "log",
    "body": [
      "console.log($1);"
    ],
    "description": "Console log statement"
  }
}
```

3. **スニペットの使用**
   - エディタで `log` と入力
   - Tab キーでスニペットを展開

### タスクの自動化
**タスクの設定：**
1. **tasks.json の作成**
   - .vscode フォルダに tasks.json を作成

2. **タスクの定義**
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Build Project",
      "type": "shell",
      "command": "npm run build",
      "group": "build"
    }
  ]
}
```

3. **タスクの実行**
   - Cmd+Shift+P → Tasks: Run Task
   - 定義したタスクを選択

### デバッグ設定
**launch.json の設定：**
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Launch Program",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/app.js"
    }
  ]
}
```

## 5. パフォーマンス最適化

### 拡張機能の最適化
**メモリ使用量の確認：**
- Help → Process Explorer
- 各拡張機能のメモリ使用量を確認

**不要な拡張機能の無効化：**
- 使用頻度の低い拡張機能を無効化
- 類似機能の拡張機能を一つに絞る

### 設定の最適化
**パフォーマンス向上の設定：**
```json
{
  "files.watcherExclude": {
    "**/node_modules/**": true,
    "**/dist/**": true
  },
  "search.exclude": {
    "**/node_modules": true,
    "**/bower_components": true
  },
  "editor.minimap.enabled": false,
  "workbench.enableExperiments": false
}
```

### キャッシュの管理
**キャッシュのクリア：**
- 定期的なキャッシュクリア
- 不要なファイルの削除

## 6. バックアップ・復元

### 設定のバックアップ
**手順：**
1. **設定ファイルのエクスポート**
   - settings.json のコピー
   - keybindings.json のコピー

2. **拡張機能リストの保存**
   - インストール済み拡張機能のリスト作成
   - 設定ファイルの保存

3. **スニペットのバックアップ**
   - カスタムスニペットの保存
   - タスク設定の保存

### 設定の復元
**手順：**
1. **設定ファイルの復元**
   - バックアップした設定ファイルを配置
   - 設定の確認

2. **拡張機能の再インストール**
   - 保存したリストから拡張機能を再インストール
   - 設定の復元

3. **動作確認**
   - 各機能の動作確認
   - 必要に応じて設定を調整

## 7. コミュニティ・リソース

### 公式リソース
- **公式ドキュメント**: [docs.cursor.sh](https://docs.cursor.sh/)
- **GitHub**: [github.com/getcursor/cursor](https://github.com/getcursor/cursor)
- **Discord**: [discord.gg/cursor](https://discord.gg/cursor)

### コミュニティリソース
- **Reddit**: r/cursor
- **Stack Overflow**: cursor タグ
- **YouTube**: Cursor チュートリアル

### 学習リソース
- **公式チュートリアル**: 基本から応用まで
- **コミュニティガイド**: ユーザー作成のガイド
- **動画チュートリアル**: 視覚的な学習

---
次は→ [[Cursor_Community_Links|参考リンク・コミュニティ]] 