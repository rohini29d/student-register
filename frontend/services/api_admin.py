import requests

API_URL = "http://127.0.0.1:8000"

def login_admin(username, password):
    return requests.post(f"{API_URL}/admin/login", json={
        "username": username,
        "password": password
    })

def upload_csv(file):
    return requests.post(f"{API_URL}/admin/upload-csv", files={
        "file": (file.name, file, "text/csv")
    })

def get_all_students():
    return requests.get(f"{API_URL}/admin/students")

def get_performance():
    return requests.get(f"{API_URL}/admin/performance")
