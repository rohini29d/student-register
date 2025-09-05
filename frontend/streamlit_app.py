import streamlit as st

# Importing each page's router with error handling
try:
    from routers import (
        student_login,
        student_register,
        take_quiz,
        view_results,
        admin_login,
        upload_csv,
        view_students,
        view_performance
    )
except ModuleNotFoundError as e:
    st.error(f"Router Import Error: {e}")
    st.stop()

st.set_page_config(page_title="Student Quiz Portal", layout="centered")
st.title("📚 Student Quiz Portal")

# Sidebar menu
menu = st.sidebar.selectbox("Navigate", [
    "Student Register",
    "Student Login",
    "Take Quiz",
    "View Results",
    "Admin Login",
    "Upload CSV",
    "View Students",
    "View Performance"
])

# Routing logic
try:
    if menu == "Student Register":
        student_register.render()
    elif menu == "Student Login":
        student_login.render()
    elif menu == "Take Quiz":
        take_quiz.render()
    elif menu == "View Results":
        view_results.render()
    elif menu == "Admin Login":
        admin_login.render()
    elif menu == "Upload CSV":
        upload_csv.render()
    elif menu == "View Students":
        view_students.render()
    elif menu == "View Performance":
        view_performance.render()
except AttributeError as e:
    st.error(f"Render Error: {e}. Make sure each router has a `render()` function.")
