import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

def render():
    st.subheader("Student Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        res = requests.post(f"{API_URL}/student/login", json={
            "email": email,
            "password": password
        })
        if res.status_code == 200:
            data = res.json()
            st.session_state["student_id"] = data["student_id"]
            st.success(f"Welcome {data['name']}!")
        else:
            st.error("Invalid Credentials")
