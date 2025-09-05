import streamlit as st

def is_logged_in():
    return "student_id" in st.session_state

def login(student_id):
    st.session_state["student_id"] = student_id

def logout():
    if "student_id" in st.session_state:
        del st.session_state["student_id"]
