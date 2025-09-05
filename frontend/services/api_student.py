import requests

API_URL = "http://127.0.0.1:8000"

def register_student(name, email, password):
    return requests.post(f"{API_URL}/student/register", json={
        "name": name,
        "email": email,
        "password": password
    })

def login_student(email, password):
    return requests.post(f"{API_URL}/student/login", json={
        "email": email,
        "password": password
    })

def get_student_results(student_id):
    return requests.get(f"{API_URL}/student/results/{student_id}")
