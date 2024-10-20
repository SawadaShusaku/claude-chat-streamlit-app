# Claude Chat Streamlit App

This is a Streamlit-based chat application powered by Anthropic's Claude AI. It features real-time token usage tracking and cost estimation for seamless interaction with Claude's API.

## Features

- Interactive chat interface using Streamlit
- Integration with Anthropic's Claude AI (claude-3-haiku-20240307 model)
- Real-time tracking of token usage (input and output)
- Accurate cost estimation based on current API pricing
- Session-based chat history

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your Anthropic API key in `.streamlit/secrets.toml`:
   ```
   ANTHROPIC_API_KEY = "your-api-key-here"
   ```
4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Usage

Simply type your message in the chat input and press Enter. The app will display the conversation history, token usage, and estimated cost.

## Note

Please ensure you have the necessary permissions and comply with Anthropic's terms of service when using their API.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/claude-chat-streamlit-app/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

# Claude チャット Streamlit アプリ

このアプリケーションは、AnthropicのClaude AIを利用したStreamlitベースのチャットアプリです。Claude APIとのシームレスな対話のためのリアルタイムトークン使用量追跡と費用見積もり機能を備えています。

## 特徴

- Streamlitを使用した対話型チャットインターフェース
- AnthropicのClaude AI（claude-3-haiku-20240307モデル）との統合
- トークン使用量（入力と出力）のリアルタイム追跡
- 現在のAPI価格に基づく正確な費用見積もり
- セッションベースのチャット履歴

## セットアップ

1. このリポジトリをクローンします
2. 必要な依存関係をインストールします:
   ```
   pip install -r requirements.txt
   ```
3. `.streamlit/secrets.toml`にAnthropicのAPIキーを設定します:
   ```
   ANTHROPIC_API_KEY = "your-api-key-here"
   ```
4. Streamlitアプリを実行します:
   ```
   streamlit run app.py
   ```

## 使用方法

チャット入力欄にメッセージを入力してEnterキーを押すだけです。アプリは会話履歴、トークン使用量、および見積もり費用を表示します。

## 注意

APIを使用する際は、必要な許可を得ていること、およびAnthropicの利用規約を遵守していることを確認してください。

## 貢献

貢献、問題の報告、機能リクエストを歓迎します。貢献したい場合は、[問題ページ](https://github.com/yourusername/claude-chat-streamlit-app/issues)をチェックしてください。

## ライセンス

[MIT](https://choosealicense.com/licenses/mit/)
