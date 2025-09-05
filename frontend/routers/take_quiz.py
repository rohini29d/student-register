import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

def render():
    if 'student_id' not in st.session_state:
        st.warning("Please login first.")
        return

    st.title("Take a Quiz")
    topic = st.text_input("Enter Topic (e.g. Python, HTML, CSS)")

    if st.button("Load Quiz"):
        try:
            res = requests.get(f"{API_URL}/quiz/questions/{topic}")
            if res.status_code != 200:
                st.error(f"Error loading quiz: {res.status_code} - {res.text}")
                return

            questions = res.json()
            if not questions:
                st.warning("No questions found for this topic.")
                return

            # Store answers and question ids in session to persist after button clicks
            if 'quiz_answers' not in st.session_state:
                st.session_state.quiz_answers = {}
                st.session_state.q_ids = []

            st.session_state.q_ids.clear()
            st.session_state.quiz_answers.clear()

            for q in questions:
                st.write(f"**Q: {q['question']}**")
                selected = st.radio(
                    "Options",
                    [q['option_a'], q['option_b'], q['option_c'], q['option_d']],
                    key=str(q['id'])  # unique key for Streamlit component
                )
                st.session_state.quiz_answers[str(q['id'])] = selected[0].upper()
                st.session_state.q_ids.append(q['id'])

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
            return

    if st.button("Submit Quiz"):
        if 'quiz_answers' not in st.session_state or not st.session_state.quiz_answers:
            st.warning("No quiz loaded or no answers selected.")
            return

        submission = {
            "student_id": st.session_state['student_id'],
            "topic": topic,
            "questions": st.session_state.q_ids,
            "answers": [st.session_state.quiz_answers[str(qid)] for qid in st.session_state.q_ids]
        }

        try:
            res = requests.post(f"{API_URL}/quiz/submit", json=submission)
            if res.status_code != 200:
                st.error(f"Submission failed: {res.status_code} - {res.text}")
                return

            result = res.json()
            st.success(f"✅ Score: {result['score']} / 10")
            st.info(f"💡 Feedback:\n{result['feedback']}")

        except requests.exceptions.RequestException as e:
            st.error(f"Submission failed: {e}")
