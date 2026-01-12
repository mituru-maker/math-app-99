import streamlit as st
import random

st.title("🔢 99×99 暗記特訓")

if 'a' not in st.session_state:
    st.session_state.a = random.randint(1, 99)
    st.session_state.b = random.randint(1, 99)

st.write(f"## 問題： {st.session_state.a} × {st.session_state.b} = ?")

answer = st.number_input("答えを入力してください", min_value=0, value=0)

if st.button("答え合わせ"):
    correct = st.session_state.a * st.session_state.b
    if answer == correct:
        st.success(f"正解！ {st.session_state.a} × {st.session_state.b} = {correct}")
        if st.button("次の問題へ"):
            st.session_state.a = random.randint(1, 99)
            st.session_state.b = random.randint(1, 99)
            st.rerun()
    else:
        st.error(f"残念！正解は {correct} です。")