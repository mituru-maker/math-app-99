import streamlit as st
import random

st.set_page_config(page_title="99x99 特訓モード", page_icon="🔢")
st.title("🔢 99×99 特訓（5問連続）")

# 問題をセッションに保持
if 'questions' not in st.session_state:
    st.session_state.questions = [(random.randint(1, 99), random.randint(1, 99)) for _ in range(5)]
    st.session_state.submitted = False

# 5問の入力欄を作成
user_answers = []
for i, (a, b) in enumerate(st.session_state.questions):
    ans = st.number_input(f"第 {i+1} 問： {a} × {b} = ", min_value=0, key=f"q{i}")
    user_answers.append(ans)

# 答え合わせボタン
if st.button("答え合わせ"):
    st.session_state.submitted = True

# 結果表示
if st.session_state.submitted:
    correct_count = 0
    st.write("---")
    for i, (a, b) in enumerate(st.session_state.questions):
        correct = a * b
        if user_answers[i] == correct:
            st.success(f"第 {i+1} 問： 正解！ ({a}×{b}={correct})")
            correct_count += 1
        else:
            st.error(f"第 {i+1} 問： ざんねん！正解は {correct} です。")
    
    st.info(f"結果： 5問中 {correct_count} 問正解！")

    # 次の問題ボタン
    if st.button("次の5問に挑戦！"):
        st.session_state.questions = [(random.randint(1, 99), random.randint(1, 99)) for _ in range(5)]
        st.session_state.submitted = False
        st.rerun()