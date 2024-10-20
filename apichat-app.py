# APIを用いたシンプルなチャットアプリ(トークンの計算機能付き)

import streamlit as st
from anthropic import Anthropic

# Anthropic APIキーを設定
api_key = st.secrets["ANTHROPIC_API_KEY"]
client = Anthropic(api_key=api_key)

st.title("Claude ChatBOT APP")

# トークン使用量と料金を表示するための変数を初期化
if "total_input_tokens" not in st.session_state:
    st.session_state.total_input_tokens = 0
if "total_output_tokens" not in st.session_state:
    st.session_state.total_output_tokens = 0
if "total_cost" not in st.session_state:
    st.session_state.total_cost = 0

# チャット履歴を保存するためのセッション状態変数
if "messages" not in st.session_state:
    st.session_state.messages = []

# チャット履歴の表示
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# チャット入力
if prompt := st.chat_input("何か言ってください", key='chat-prompt'):
    # ユーザーの入力をメッセージリストに追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Claude APIを呼び出してレスポンスを取得
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[
            *st.session_state.messages
        ]
    )
    
    # ボットの応答をメッセージリストに追加
    assistant_message = response.content[0].text
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
    
    # トークン使用量の更新
    st.session_state.total_input_tokens += response.usage.input_tokens
    st.session_state.total_output_tokens += response.usage.output_tokens
    
    # コストの計算（MTokあたりの料金を使用）
    input_cost = (st.session_state.total_input_tokens / 1_000_000) * 0.25
    output_cost = (st.session_state.total_output_tokens / 1_000_000) * 1.25
    st.session_state.total_cost = input_cost + output_cost
    
    # ページを再読み込みして新しいメッセージを表示
    st.rerun()

# トークン使用量と料金を表示
st.subheader(f"Total input tokens: {st.session_state.total_input_tokens}")
st.subheader(f"Total output tokens: {st.session_state.total_output_tokens}")
st.subheader(f"Total tokens: {st.session_state.total_input_tokens + st.session_state.total_output_tokens}")
st.subheader(f"Total cost: ${st.session_state.total_cost:.6f}")