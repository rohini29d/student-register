import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

def render():
    st.subheader("Register as a Student")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        # Validate input
        if not name or not email or not password:
            st.warning("All fields are required!")
            return

        try:
            res = requests.post(f"{API_URL}/student/register", json={
                "name": name,
                "email": email,
                "password": password
            })

            if res.status_code == 200:
                st.success("Successfully Registered!")
            else:
                try:
                    st.error(res.json().get("detail", "Registration failed."))
                except Exception:
                    st.error("An unknown error occurred during registration.")

        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to the backend server. Is FastAPI running?")
