# frontend.py
import streamlit as st
import requests
import os

st.set_page_config(page_title="🌏 Travel Assistant Chatbot", layout="centered")

st.title("🌏 Travel Assistant — Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

backend_url = st.text_input("Backend URL (if not localhost):", value=os.environ.get("BACKEND_URL", "http://localhost:8000")).strip().rstrip("/")

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", "")
    submit = st.form_submit_button("Send")

if submit and user_input:
    payload = {"message": user_input}
    try:
        r = requests.post(f"{backend_url}/chat", json=payload, timeout=30)
        if r.status_code == 200:
            data = r.json()
            bot_text = data.get("response", "⚠️ No response field in backend JSON")
            backend_name = data.get("backend", "unknown")
            display_bot = f"{bot_text}  \n\n_(from: {backend_name})_"
        else:
            display_bot = f"⚠️ Backend error {r.status_code}: {r.text}"
    except Exception as e:
        display_bot = f"⚠️ Request failed: {e}"

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", display_bot))

st.markdown("### Conversation")
for speaker, message in st.session_state.history:
    if speaker == "You":
        st.markdown(f"<div style='text-align:right; color: #0b5cff;'><strong>{speaker}:</strong> {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align:left; color: #067d68;'><strong>{speaker}:</strong> {message}</div>", unsafe_allow_html=True)
    st.write("---")
