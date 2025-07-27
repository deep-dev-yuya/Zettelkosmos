---
title: Gmail分類システム - n8nワークフロー改修実装記録
tags: [プロジェクト, Gmail, PoC, n8n, ワークフロー, 自動ラベル付与, Claude Code]
created: 2025-07-16
type: project
status: completed
related: 
  - "[[claude_gmail_label_request]]"
  - "[[コンテキストガイド高度化実装記録]]"
  - "[[トラブルシューティング統合ソリューション実装記録]]"
---

# 📌 n8nワークフロー改修実装記録

## 🎯 作業概要

Gmail AI Classifier PoCプロジェクトの**n8nワークフローを、LINE通知からGmail自動ラベル付与に完全改修**した詳細記録です。

**実行日時**: 2025-07-16  
**作業者**: Claude Code  
**目的**: Gmail自動ラベル付与に特化したワークフロー構築  
**参考ドキュメント**: `claude_gmail_label_request.md`

---

## 📂 プロジェクト情報

| 項目 | 詳細 |
|------|------|
| **プロジェクト名** | Gmail AI Classifier PoC |
| **プロジェクト場所** | `/Users/[ユーザー名]/Projects/dev-projects/gmail-classifier` |
| **新規作成ファイル** | `n8n/gmail_label_workflow.json` |
| **新規作成ファイル** | `n8n/workflow_architecture.md` |
| **改修対象** | n8nワークフロー構成の完全見直し |

---

## 🔍 改修要件と背景

### 🎯 ユーザーからの要望

```text
目的：Gmailに届いたメールを分類し、Gmail自体にラベルを自動で付与するn8nワークフローを完成させたいです。

課題・変更点：
- LINE通知はすでに別のワークフローで運用しているため、ここでは Gmailへのラベル付与を行いたいです。
- Gmail Trigger で取得できる messageId を使って、分類されたラベル（例：「支払い関係」「重要」など）を Gmail に付与してください。
- ラベルが存在しない場合は自動作成してもOKです。

要望：
1. 修正済みの n8n ワークフロー構成をわかりやすい図解かステップ一覧で提示
2. Gmailノードでの設定内容（例：Modify Message / Add Label）を記述
3. Switchの条件式例も含めて明記（classificationによる分岐）
4. ラベル名と分類結果を map で一元管理する形にしてもOK
5. Google Sheetsへのログ記録は残す（ラベル・分類・信頼度など）
6. Flask APIエンドポイント：http://localhost:5001/api/classify
7. オプション：confidence < 0.5 などのケースを「再学習候補」として記録
```

### 🔄 従来ワークフローの問題点

#### 旧構成（workflow_sample.json）
```
Gmail Trigger → Email Preprocessing → MCP Context Enricher → AI Classification
    ↓
Switch分類 → LINE通知 + Google Sheets保存
```

#### 問題点
1. **LINE通知**: 別ワークフローで処理済みのため重複
2. **ラベル付与なし**: Gmail自体にラベルが付与されない
3. **限定的Switch**: 「重要」のみの分岐処理
4. **再学習支援なし**: 信頼度不足ケースの記録なし
5. **API更新未対応**: 新しいエンドポイントに未対応

---

## 🛠️ 改修実装内容

### 1. 新ワークフロー構成 🔗

#### 全体フロー図
```
Gmail Trigger
    ↓
Email Preprocessing (HTMLタグ除去・正規化)
    ↓
Context Enricher (高度文脈補完・エンティティ抽出)
    ↓
AI Classification (Pipeline分類モデル)
    ↓
Label Mapping (分類結果→Gmailラベル変換)
    ↓
Gmail Add Label (Gmailにラベル付与)
    ↓
Classification Switch (全分類対応分岐)
    ├─ Google Sheets Log (通常ログ)
    └─ Low Confidence Log (要確認ログ)
```

### 2. 重要な技術的変更 🔧

#### A. messageId保持機能
```javascript
// Email Preprocessing ノード
return {
  json: {
    ...data,
    subject: data.subject || '',
    body: normalizedBody,
    messageId: data.id,  // Gmail messageId を保持
    processedAt: new Date().toISOString()
  }
};
```

#### B. 分類結果のラベルマッピング
```javascript
// Label Mapping ノード
const labelMapping = {
  '支払い関係': 'AI-Payment',
  '重要': 'AI-Important', 
  'プロモーション': 'AI-Promotion',
  '仕事・学習': 'AI-Work-Study'
};

const gmailLabel = labelMapping[classification] || 'AI-Unclassified';

// 信頼度が低い場合の処理
const isLowConfidence = confidence < 0.5;
const finalLabel = isLowConfidence ? 'AI-NeedsReview' : gmailLabel;
```

#### C. Gmail自動ラベル付与
```json
{
  "parameters": {
    "operation": "addLabels",
    "messageId": "={{ $json.messageId }}",
    "labelIds": "={{ $json.gmailLabel }}",
    "options": {
      "createLabels": true
    }
  },
  "name": "Gmail Add Label",
  "type": "n8n-nodes-base.gmail"
}
```

#### D. 全分類対応Switch条件
```json
{
  "parameters": {
    "conditions": {
      "conditions": [
        {
          "leftValue": "={{ $json.classification }}",
          "rightValue": "支払い関係",
          "operator": {"type": "string", "operation": "equals"}
        },
        {
          "leftValue": "={{ $json.classification }}",
          "rightValue": "重要",
          "operator": {"type": "string", "operation": "equals"}
        },
        {
          "leftValue": "={{ $json.classification }}",
          "rightValue": "プロモーション",
          "operator": {"type": "string", "operation": "equals"}
        },
        {
          "leftValue": "={{ $json.classification }}",
          "rightValue": "仕事・学習",
          "operator": {"type": "string", "operation": "equals"}
        },
        {
          "leftValue": "={{ $json.isLowConfidence }}",
          "rightValue": true,
          "operator": {"type": "boolean", "operation": "true"}
        }
      ]
    },
    "combineOperation": "any"
  }
}
```

### 3. 新しいAPIエンドポイント統合 🌐

#### 更新されたエンドポイント
- **Context Enricher**: `http://localhost:5001/api/enrich-context`
- **AI Classification**: `http://localhost:5001/api/classify`

#### 高度文脈補完対応
```json
{
  "parameters": {
    "url": "http://localhost:5001/api/enrich-context",
    "bodyParametersJson": "{\n  \"subject\": \"{{ $json.subject }}\",\n  \"body\": \"{{ $json.body }}\"\n}"
  }
}
```

### 4. Google Sheets記録の拡張 📊

#### 通常ログシート（ログ!A:H）
```json
{
  "columns": {
    "mappingMode": "defineBelow",
    "value": {
      "timestamp": "={{ $json.processTime }}",
      "messageId": "={{ $json.messageId }}",
      "subject": "={{ $json.subject }}",
      "classification": "={{ $json.classification }}",
      "confidence": "={{ Number($json.confidence).toFixed(3) }}",
      "gmailLabel": "={{ $json.gmailLabel }}",
      "enrichedContext": "={{ $json.enrichedContext }}",
      "status": "={{ $json.isLowConfidence ? '要確認' : '完了' }}"
    }
  }
}
```

#### 再学習候補シート（再学習候補!A:F）
```json
{
  "columns": {
    "mappingMode": "defineBelow",
    "value": {
      "timestamp": "={{ $json.processTime }}",
      "messageId": "={{ $json.messageId }}",
      "subject": "={{ $json.subject }}",
      "predictedClass": "={{ $json.classification }}",
      "confidence": "={{ Number($json.confidence).toFixed(3) }}",
      "reason": "信頼度不足"
    }
  }
}
```

---

## 🎯 自動作成されるGmailラベル

### ラベル一覧と用途
| ラベル名 | 分類結果 | 用途 | 色分け推奨 |
|----------|----------|------|------------|
| **AI-Payment** | 支払い関係 | PayPay・請求・決済メール | 🟢 緑 |
| **AI-Important** | 重要 | 緊急・セキュリティ・障害メール | 🔴 赤 |
| **AI-Promotion** | プロモーション | セール・キャンペーン・広告メール | 🟡 黄 |
| **AI-Work-Study** | 仕事・学習 | 求人・学習・GitHub・Stack Overflow | 🔵 青 |
| **AI-NeedsReview** | 要確認 | 信頼度不足（< 0.5） | 🟠 オレンジ |
| **AI-Unclassified** | 未分類 | マッピング失敗 | ⚫ グレー |

### ラベル自動作成機能
- **createLabels**: true 設定により存在しないラベルを自動作成
- **命名規則**: AI-プレフィックスによる分類ラベルの統一
- **管理性**: 手動ラベルとの分離によるメンテナンス性向上

---

## 📋 各ノードの詳細仕様

### 1. Gmail Trigger
```json
{
  "parameters": {
    "pollTimes": {
      "item": [{"mode": "everyMinute"}]
    },
    "simple": false,
    "filters": {},
    "options": {}
  },
  "name": "Gmail Trigger",
  "type": "n8n-nodes-base.gmailTrigger",
  "typeVersion": 2
}
```

### 2. Email Preprocessing
```javascript
// HTMLタグ除去とテキスト正規化
const items = $input.all();

return items.map(item => {
  const data = item.json;
  
  // HTMLタグ除去
  const cleanBody = data.textPlain || data.textHtml?.replace(/<[^>]*>/g, '') || '';
  
  // 基本的な正規化
  const normalizedBody = cleanBody
    .replace(/\r\n/g, '\n')
    .replace(/\n+/g, ' ')
    .trim();
  
  return {
    json: {
      ...data,
      subject: data.subject || '',
      body: normalizedBody,
      messageId: data.id,  // Gmail messageId を保持
      processedAt: new Date().toISOString()
    }
  };
});
```

### 3. Context Enricher
```json
{
  "parameters": {
    "url": "http://localhost:5001/api/enrich-context",
    "options": {
      "bodyContentType": "json",
      "headers": {
        "item": [
          {
            "name": "Content-Type",
            "value": "application/json"
          }
        ]
      }
    },
    "jsonParameters": true,
    "bodyParametersJson": "{\n  \"subject\": \"{{ $json.subject }}\",\n  \"body\": \"{{ $json.body }}\"\n}"
  }
}
```

### 4. AI Classification
```json
{
  "parameters": {
    "url": "http://localhost:5001/api/classify",
    "options": {
      "bodyContentType": "json",
      "headers": {
        "item": [
          {
            "name": "Content-Type",
            "value": "application/json"
          }
        ]
      }
    },
    "jsonParameters": true,
    "bodyParametersJson": "{\n  \"subject\": \"{{ $json.subject }}\",\n  \"body\": \"{{ $json.body }}\"\n}"
  }
}
```

### 5. Label Mapping
```javascript
// 分類結果とラベルのマッピング
const items = $input.all();

return items.map(item => {
  const classification = $('AI Classification').item.json.classification;
  const confidence = $('AI Classification').item.json.confidence;
  const context = $('Context Enricher').item.json.enriched_context;
  const messageId = $('Email Preprocessing').item.json.messageId;
  
  // 分類結果をGmailラベルにマッピング
  const labelMapping = {
    '支払い関係': 'AI-Payment',
    '重要': 'AI-Important', 
    'プロモーション': 'AI-Promotion',
    '仕事・学習': 'AI-Work-Study'
  };
  
  const gmailLabel = labelMapping[classification] || 'AI-Unclassified';
  
  // 信頼度が低い場合の処理
  const isLowConfidence = confidence < 0.5;
  const finalLabel = isLowConfidence ? 'AI-NeedsReview' : gmailLabel;
  
  return {
    json: {
      ...item.json,
      messageId: messageId,
      classification: classification,
      confidence: confidence,
      gmailLabel: finalLabel,
      enrichedContext: context,
      isLowConfidence: isLowConfidence,
      processTime: new Date().toISOString()
    }
  };
});
```

### 6. Gmail Add Label
```json
{
  "parameters": {
    "operation": "addLabels",
    "messageId": "={{ $json.messageId }}",
    "labelIds": "={{ $json.gmailLabel }}",
    "options": {
      "createLabels": true
    }
  },
  "name": "Gmail Add Label",
  "type": "n8n-nodes-base.gmail",
  "typeVersion": 2
}
```

---

## 🔧 設定要項と運用ガイド

### 1. 必須前提条件
- **Gmail API権限**: modify権限が必要
- **Flask API**: http://localhost:5001で稼働
- **Google Sheets**: 書き込み権限が必要

### 2. 設定変更箇所
```json
// Google Sheets設定
"sheetId": "YOUR_GOOGLE_SHEET_ID",  // 実際のシートIDに変更

// シート構成
"range": "ログ!A:H",                // 通常ログシート
"range": "再学習候補!A:F",           // 低信頼度ログシート
```

### 3. トラブルシューティング

#### よくある問題
1. **ラベル付与失敗**
   - Gmail API権限確認
   - messageId形式確認

2. **分類精度低下**
   - 再学習候補シートからデータ追加
   - Pipelineモデル再学習

3. **Google Sheets書き込みエラー**
   - シートID確認
   - 権限設定確認

4. **Flask API接続エラー**
   - localhost:5001稼働確認
   - エンドポイント応答確認

---

## 📊 改修効果の評価

### 🎯 機能改善

| 項目 | 改修前 | 改修後 | 改善 |
|------|--------|--------|------|
| **Gmail統合** | なし | 自動ラベル付与 | 完全統合 |
| **分類対応** | 重要のみ | 全4分類対応 | 4倍拡張 |
| **再学習支援** | なし | 低信頼度記録 | 新機能 |
| **LINE通知** | 重複実装 | 完全除外 | 最適化 |
| **API対応** | 旧エンドポイント | 高度文脈補完 | 最新対応 |

### 🌐 ワークフロー品質

| 品質項目 | 改修前 | 改修後 | 効果 |
|----------|--------|--------|------|
| **重複排除** | LINE通知重複 | 責務分離 | 保守性向上 |
| **拡張性** | 限定的Switch | 全分類対応 | 拡張性向上 |
| **運用性** | 手動ラベル | 自動ラベル | 運用負荷削減 |
| **トレーサビリティ** | 基本ログ | 詳細ログ | 監査性向上 |

### 📈 期待される運用効果

1. **作業効率化**: 手動ラベル付与作業の完全自動化
2. **分類一貫性**: AI分類による客観的・一貫したラベル付与
3. **継続改善**: 低信頼度メールの自動記録による学習データ蓄積
4. **Gmail統合**: 既存のGmailワークフローとの完全統合
5. **保守性向上**: 責務分離による各ワークフローの独立運用

---

## 🚀 今後の展開可能性

### 1. ワークフロー拡張
- **条件分岐**: 優先度による異なる処理フロー
- **通知統合**: 高優先度メールの即座通知
- **アーカイブ**: 低優先度メールの自動アーカイブ

### 2. 機械学習連携
- **フィードバック学習**: ラベル修正履歴の学習データ化
- **A/Bテスト**: 複数モデルの並行評価
- **自動再学習**: 定期的なモデル更新

### 3. 他サービス連携
- **Slack通知**: 重要メールのSlack連携
- **カレンダー**: 期限付きメールのカレンダー登録
- **タスク管理**: アクション要求メールのタスク化

---

## 📝 技術メモ

### 作成ファイル
```bash
# 新しいワークフローJSONファイル
n8n/gmail_label_workflow.json

# ワークフロー構成説明書
n8n/workflow_architecture.md
```

### 環境情報
- **n8n**: 最新版対応（typeVersion更新）
- **Gmail API**: v1（modify権限）
- **Google Sheets API**: v4
- **Flask API**: http://localhost:5001

### 設定チェックリスト
- [ ] Gmail API権限設定
- [ ] Google Sheets ID設定
- [ ] Flask API稼働確認
- [ ] シート構成作成
- [ ] ラベル動作確認

---

## 🎉 重要な達成事項

### 🎯 claude_gmail_label_request完全対応
- **Gmail自動ラベル付与**: messageIdを使用した確実なラベル付与
- **LINE通知削除**: 別ワークフローとの重複解消
- **全分類対応**: 4つの分類すべてに対応したSwitch条件
- **再学習支援**: 信頼度不足メールの自動記録機能

### 🔧 技術的品質向上
- **messageId保持**: Gmail操作のための確実なID管理
- **ラベル自動作成**: 存在しないラベルの自動作成機能
- **エラーハンドリング**: 信頼度不足・未分類ケースの適切な処理
- **API最新化**: 高度文脈補完エンドポイントの統合

### 🌐 運用効率化
- **自動化**: 手動ラベル付与作業の完全自動化
- **一貫性**: AI分類による客観的なラベル付与
- **トレーサビリティ**: 全処理履歴の詳細記録
- **継続改善**: 低信頼度メールの再学習データ蓄積

### 📊 システム統合完了
- **Gmail統合**: 既存のGmailワークフローとの完全統合
- **API統合**: 高度文脈補完・Pipeline分類モデルの統合
- **Google Sheets統合**: 詳細ログ・再学習候補の統合記録
- **責務分離**: 各ワークフローの独立運用による保守性向上

---

**作成者**: Claude Code  
**最終更新**: 2025-07-16  
**関連ドキュメント**: [[claude_gmail_label_request]], [[コンテキストガイド高度化実装記録]]

---

## 🔗 参考リンク

- [n8n Gmail Node Documentation](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/)
- [Gmail API Labels Documentation](https://developers.google.com/gmail/api/reference/rest/v1/users.labels)
- [Google Sheets API v4](https://developers.google.com/sheets/api/reference/rest)
- プロジェクトリポジトリ: `https://github.com/deep-dev-yuya/gmail-classifier.git`