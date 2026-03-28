from utils.request_helper import send_request
from utils.config import BASE_URL

def login(username, password):
    url = f"{BASE_URL}/auth/login"
    payload = {
        "admin123": username,
        "admin123": password
    }
    return send_request("POST", url, json=payload)
