#!/usr/bin/env python3
"""
Gmail分類PoC - 拡張版カスタマイズ学習データ
あなたの実際のメールパターン + 追加サービス対応版
"""

import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

def create_extended_training_data():
    """拡張版学習データ作成（あなたのメール + 追加サービス）"""
    
    training_data = [
        # === 支払い・金融関係（15件）===
        {
            "subject": "【デビットカード】ご利用のお知らせ(住信SBI ネット銀行)",
            "body": "デビットカードのご利用がありました。利用日時: 2025/07/16 利用加盟店: OPENAI *CHATGPT SUBSCR 引落金額: 3,360円",
            "label": "支払い関係"
        },
        {
            "subject": "クレジットカード利用明細",
            "body": "今月のクレジットカード利用明細をお送りします。ご確認ください。",
            "label": "支払い関係"
        },
        {
            "subject": "電気料金のお知らせ",
            "body": "今月の電気使用量と料金のお知らせです。お支払い期限にご注意ください。",
            "label": "支払い関係"
        },
        {
            "subject": "PayPay残高チャージ完了",
            "body": "PayPay残高へのチャージが完了しました。チャージ金額: 5,000円",
            "label": "支払い関係"
        },
        {
            "subject": "Amazon 注文確認",
            "body": "ご注文いただきありがとうございます。注文番号: 123-4567890-1234567",
            "label": "支払い関係"
        },
        {
            "subject": "楽天カード ご利用代金明細",
            "body": "楽天カードのご利用代金明細書を発行いたしました。",
            "label": "支払い関係"
        },
        {
            "subject": "ペイディ今月のご利用明細",
            "body": "ペイディをご利用いただきありがとうございます。今月のご利用金額をお知らせします。",
            "label": "支払い関係"
        },
        {
            "subject": "povo 月額料金のお知らせ",
            "body": "povo2.0の今月のご利用料金が確定いたしました。トッピング料金を含みます。",
            "label": "支払い関係"
        },
        {
            "subject": "Netflix 月額料金のお知らせ",
            "body": "Netflix月額料金のお支払いを確認いたしました。",
            "label": "支払い関係"
        },
        {
            "subject": "Spotify Premium 料金決済完了",
            "body": "Spotify Premiumの月額料金の決済が完了しました。",
            "label": "支払い関係"
        },
        {
            "subject": "水道料金のお知らせ",
            "body": "水道使用量のお知らせと料金請求書をお送りします。",
            "label": "支払い関係"
        },
        {
            "subject": "ガス料金請求書",
            "body": "今月のガス使用料金をお知らせいたします。口座振替日をご確認ください。",
            "label": "支払い関係"
        },
        {
            "subject": "Apple Store 購入レシート",
            "body": "App Store & iTunes での購入ありがとうございます。購入内容をご確認ください。",
            "label": "支払い関係"
        },
        {
            "subject": "Udemy 領収書",
            "body": "Udemyコースの購入ありがとうございます。領収書を添付いたします。",
            "label": "支払い関係"
        },
        {
            "subject": "GitHub Pro 請求書",
            "body": "GitHub Proプランの月額料金をお知らせします。",
            "label": "支払い関係"
        },
        
        # === プロモーション・お得情報（12件）===
        {
            "subject": "今週の新着・おすすめ情報！",
            "body": "セブンマイルプログラムからのお知らせ 新着の特典・おすすめ特典をご紹介！",
            "label": "プロモーション"
        },
        {
            "subject": "Amazonギフトカード【50,000円分】が当たるチャンス！",
            "body": "Gポイント懸賞に応募しよう！最大40000リワードの還元で家計を応援する限定プログラム",
            "label": "プロモーション"
        },
        {
            "subject": "【エグゼクティブ会員限定】ミツウロコでんき限定プログラムのご案内",
            "body": "電気代の削減だけでなく会員様へ最大40000リワードの還元で家計を応援",
            "label": "プロモーション"
        },
        {
            "subject": "楽天市場 お買い物マラソン開催中",
            "body": "期間限定！ポイント最大43倍のチャンス。この機会をお見逃しなく！",
            "label": "プロモーション"
        },
        {
            "subject": "Amazon タイムセール情報",
            "body": "本日限定のタイムセール商品をご紹介します。お急ぎください！",
            "label": "プロモーション"
        },
        {
            "subject": "PayPayボーナス獲得のチャンス",
            "body": "対象店舗でのお支払いでPayPayボーナスが最大20%還元！",
            "label": "プロモーション"
        },
        {
            "subject": "Udemy 夏のビッグセール開催中",
            "body": "人気コースが最大90%OFF！プログラミング、デザイン、ビジネススキルのコースが特価です。",
            "label": "プロモーション"
        },
        {
            "subject": "Indeed プレミアム会員特典のご案内",
            "body": "Indeed プレミアム会員限定の求人情報と転職サポートをご利用ください。",
            "label": "プロモーション"
        },
        {
            "subject": "Remogu キャッシュバックキャンペーン",
            "body": "リモートワーク支援サービス Remogu のキャッシュバックキャンペーン実施中！",
            "label": "プロモーション"
        },
        {
            "subject": "povo 追加トッピング10%オフ",
            "body": "期間限定！povoの追加データトッピングが10%オフでご利用いただけます。",
            "label": "プロモーション"
        },
        {
            "subject": "無料体験キャンペーン実施中",
            "body": "新サービスの無料体験を実施しています。この機会にぜひお試しください。",
            "label": "プロモーション"
        },
        {
            "subject": "限定クーポンをお送りします",
            "body": "会員様限定の特別クーポンをご用意いたしました。有効期限にご注意ください。",
            "label": "プロモーション"
        },
        
        # === 重要・システム関連（10件）===
        {
            "subject": "システムメンテナンスのお知らせ",
            "body": "システムメンテナンスを実施いたします。サービス停止時間にご注意ください。",
            "label": "重要"
        },
        {
            "subject": "パスワード変更のお知らせ",
            "body": "セキュリティ向上のため、パスワードの変更をお願いいたします。",
            "label": "重要"
        },
        {
            "subject": "ログイン通知",
            "body": "あなたのアカウントに新しいデバイスからログインがありました。",
            "label": "重要"
        },
        {
            "subject": "緊急：不正アクセスの可能性",
            "body": "アカウントに不正アクセスの可能性があります。至急パスワードを変更してください。",
            "label": "重要"
        },
        {
            "subject": "GitHub セキュリティアラート",
            "body": "リポジトリに脆弱性のある依存関係が検出されました。至急対応してください。",
            "label": "重要"
        },
        {
            "subject": "Indeed アカウント認証が必要です",
            "body": "セキュリティ確認のため、アカウントの認証手続きを完了してください。",
            "label": "重要"
        },
        {
            "subject": "Udemy アカウント一時停止の通知",
            "body": "利用規約違反の可能性があるため、一時的にアカウントを停止いたします。",
            "label": "重要"
        },
        {
            "subject": "povo 重要なお知らせ",
            "body": "サービス変更に関する重要なお知らせがあります。必ずご確認ください。",
            "label": "重要"
        },
        {
            "subject": "セキュリティアラート",
            "body": "異常なアクティビティが検出されました。アカウントを確認してください。",
            "label": "重要"
        },
        {
            "subject": "システム障害の報告",
            "body": "現在、システムで障害が発生しています。復旧作業を行っています。",
            "label": "重要"
        },
        
        # === 仕事・学習関連（8件）===
        {
            "subject": "Indeed 新着求人のお知らせ",
            "body": "あなたのスキルにマッチする新着求人をお知らせします。エンジニア職の求人が5件あります。",
            "label": "仕事・学習"
        },
        {
            "subject": "Udemy 学習進捗レポート",
            "body": "今週の学習進捗をお知らせします。Python入門コースの進捗率は75%です。",
            "label": "仕事・学習"
        },
        {
            "subject": "GitHub 週次アクティビティサマリー",
            "body": "先週のGitHubアクティビティをまとめました。コミット数、プルリクエスト数をご確認ください。",
            "label": "仕事・学習"
        },
        {
            "subject": "Remogu リモートワーク求人情報",
            "body": "フルリモート可能な新着求人をご紹介します。あなたのスキルに合致する案件があります。",
            "label": "仕事・学習"
        },
        {
            "subject": "オンライン会議のリマインド",
            "body": "明日のチームミーティングのリマインドです。Zoomリンクをご確認ください。",
            "label": "仕事・学習"
        },
        {
            "subject": "コース修了証明書の発行",
            "body": "Udemyコースを修了されました。修了証明書をダウンロードできます。",
            "label": "仕事・学習"
        },
        {
            "subject": "Indeed 応募企業からの返信",
            "body": "応募いただいた企業から選考結果のご連絡があります。",
            "label": "仕事・学習"
        },
        {
            "subject": "技術記事のおすすめ",
            "body": "あなたの興味分野に関する最新の技術記事をピックアップしました。",
            "label": "仕事・学習"
        }
    ]
    
    return pd.DataFrame(training_data)

def train_extended_model():
    """拡張版学習データでモデル訓練"""
    
    print("Gmail分類PoC - 拡張版カスタマイズ学習データでモデル訓練")
    print("=" * 70)
    
    # データ準備
    df = create_extended_training_data()
    print(f"📊 学習データ数: {len(df)}")
    print(f"🏷 分類ラベル: {list(df['label'].value_counts().index)}")
    print(f"📈 各ラベルの件数:")
    for label, count in df['label'].value_counts().items():
        print(f"  - {label}: {count}件")
    
    # テキスト結合と前処理
    X = df['subject'] + ' ' + df['body']
    y = df['label']
    
    # 特徴量抽出（TF-IDF）- 日本語に最適化
    vectorizer = TfidfVectorizer(
        max_features=3000,        # 特徴量数を増加
        ngram_range=(1, 3),       # 1-gram〜3-gramで文脈をより捉える
        stop_words=None,          # 日本語ストップワードは使用しない
        min_df=1,                 # 最小出現回数
        max_df=0.9,               # 最大出現頻度を調整
        analyzer='word',          # 単語レベル分析
        token_pattern=r'[^\s]+',  # 日本語対応のトークンパターン
    )
    
    X_vectorized = vectorizer.fit_transform(X)
    print(f"🔤 特徴量次元数: {X_vectorized.shape[1]}")
    
    # データ分割
    X_train, X_test, y_train, y_test = train_test_split(
        X_vectorized, y, test_size=0.25, random_state=42, stratify=y
    )
    
    # モデル学習（SVM）- パラメータ調整
    model = LinearSVC(
        random_state=42, 
        max_iter=20000,
        C=1.0,                    # 正則化パラメータ
        class_weight='balanced'   # クラス不均衡に対応
    )
    model.fit(X_train, y_train)
    
    # 評価
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n🎯 モデル評価")
    print(f"📊 正解率: {accuracy:.3f}")
    print("\n📋 詳細評価:")
    print(classification_report(y_test, y_pred, zero_division=0))
    
    # 特徴量の重要度（上位キーワード表示）
    print("\n🔍 各分類の重要キーワード（上位5個）:")
    feature_names = vectorizer.get_feature_names_out()
    for i, label in enumerate(model.classes_):
        # 各クラスの重要特徴量取得
        coef = model.coef_[i]
        top_indices = coef.argsort()[-5:][::-1]  # 上位5個
        top_features = [feature_names[idx] for idx in top_indices]
        print(f"  🏷 {label}: {', '.join(top_features)}")
    
    # モデル保存
    model_path = 'model.pkl'
    with open(model_path, 'wb') as f:
        pickle.dump((vectorizer, model), f)
    
    print(f"\n💾 モデルが {model_path} に保存されました")
    
    # 予測テスト
    print(f"\n🧪 予測テスト")
    test_emails = [
        ("PayPay決済完了のお知らせ コンビニでの支払いが完了しました", "支払い関係"),
        ("Udemy ビッグセール開催中 人気コースが90%オフ", "プロモーション"),
        ("緊急システム障害 サーバーに異常が発生しています", "重要"),
        ("Indeed 新着求人 あなたにマッチする求人が見つかりました", "仕事・学習"),
        ("povo データ追加 残りギガ数が少なくなっています", "プロモーション")
    ]
    
    for email_text, expected in test_emails:
        X_test_sample = vectorizer.transform([email_text])
        prediction = model.predict(X_test_sample)[0]
        probability = max(model.decision_function(X_test_sample)[0])
        
        status = "✅" if prediction == expected else "❌"
        print(f"{status} テキスト: {email_text[:40]}...")
        print(f"   予測: {prediction} (期待: {expected}) 信頼度: {probability:.2f}")
    
    return vectorizer, model

if __name__ == "__main__":
    # 仮想環境確認
    if 'VIRTUAL_ENV' in os.environ:
        print(f"🔧 仮想環境: {os.environ['VIRTUAL_ENV']}")
    else:
        print("⚠️  仮想環境が有効化されていません")
    
    vectorizer, model = train_extended_model()
    
    print(f"\n🎉 訓練完了！")
    print(f"📁 保存場所: {os.getcwd()}/model.pkl")
    print(f"🚀 次のステップ:")
    print(f"   1. Flask APIサーバーを起動: python run.py")
    print(f"   2. 動作確認: python scripts/quick_test.py")
    print(f"   3. n8nワークフローの設定")
