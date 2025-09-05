import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

def render():
    st.subheader("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        res = requests.post(f"{API_URL}/admin/login", json={
            "username": username,
            "password": password
        })
        if res.status_code == 200:
            st.session_state["admin"] = res.json()["admin_id"]
            st.success("Admin Logged in.")
        else:
            st.error("Invalid Credentials")
