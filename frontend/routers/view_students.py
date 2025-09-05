import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

def render():
    if "admin" not in st.session_state:
        st.warning("Admin login required.")
        return

    res = requests.get(f"{API_URL}/admin/students")
    students = res.json()
    st.dataframe(students)
