import requests

API_URL = "http://127.0.0.1:8000"

def get_quiz_questions(topic):
    return requests.get(f"{API_URL}/quiz/questions/{topic}")

def submit_quiz(student_id, topic, question_ids, answers):
    submission = {
        "student_id": student_id,
        "topic": topic,
        "questions": question_ids,
        "answers": answers
    }
    return requests.post(f"{API_URL}/quiz/submit", json=submission)
# In api_quiz.py
def get_available_topics():
    response = requests.get(f"{API_URL}/quiz/topics")
    if response.status_code == 200:
        return response.json()
    return []