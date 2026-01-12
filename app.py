import streamlit as st
import random

st.set_page_config(page_title="99x99 連続特訓", page_icon="🔢")
st.title("🔢 99×99 連続特訓（5問）")

# 問題の作成ロジックを更新
if 'questions' not in st.session_state:
    # 最初の数字（a）をランダムに1つ決定
    base_a = random.randint(1, 99)
    # かける相手（b）のスタート地点をランダムに決定（b+4が99を超えないように調整）
    start_b = random.randint(1, 95)
    
    # aは固定、bは1ずつ増える5問を作成
    st.session_state.questions = [(base_a, start_b + i) for i in range(5)]
    st.session_state.submitted = False

# 入力欄を表示
user_answers = []
for i, (a, b) in enumerate(st.session_state.questions):
    ans = st.number_input(f"第 {i+1} 問： {a} × {b} = ", min_value=0, key=f"q{i}", value=0)
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
    
    # 全問正解なら紙吹雪を飛ばす演出
    if correct_count == 5:
        st.balloons()
        st.info("✨ すばらしい！全問正解です！ ✨")
    else:
        st.info(f"結果： 5問中 {correct_count} 問正解！")

    # 次の問題ボタン
    if st.button("新しい段に挑戦！"):
        # セッションをリセットして再描画
        del st.session_state.questions
        st.session_state.submitted = False
        st.rerun()