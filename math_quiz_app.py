import streamlit as st
import random

st.title("📝 Math Quiz")
st.write("Test your math skills! Choose difficulty and solve the questions.")

# --- Difficulty Levels ---
difficulty = st.selectbox("Select Difficult Level:", ["Easy", "Medium", "Hard"])

# --- Question Generator ---
def generate_question(difficulty):
    if difficulty == "Easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
        return f"{a} + {b}", a + b
    elif difficulty == "Medium":
        a, b = random.randint(10, 100), random.randint(10, 100)
        return f"{a} - {b}", a - b
    else:
        a, b = random.randint(20, 60), random.randint(20, 60)
        return f"{a} × {b}", a * b

# --- Quiz Logic ---
if st.button("Generate Question"):
    question, answer = generate_question(difficulty)
    st.session_state['question'] = question
    st.session_state['answer'] = answer
    st.session_state['feedback'] = ""

if 'question' in st.session_state:
    st.write(f"**Question:** {st.session_state['question']}")
    user_answer = st.text_input("Your Answer:")
    
    if st.button("Submit Answer"):
        try:
            if int(user_answer) == st.session_state['answer']:
                st.session_state['feedback'] = "✅ Correct!"
            else:
                st.session_state['feedback'] = f"❌ Incorrect. The correct answer was {st.session_state['answer']}."
        except:
            st.session_state['feedback'] = "⚠️ Please enter a valid number."

    st.write(st.session_state['feedback'])