import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

def render():
    if "student_id" not in st.session_state:
        st.warning("Login required.")
        return

    res = requests.get(f"{API_URL}/student/results/{st.session_state['student_id']}")
    results = res.json()
    for r in results:
        st.write(f"**Topic:** {r['topic']} | **Score:** {r['score']}")
        st.info(r['feedback'])
