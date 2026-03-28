from utils.request_helper import send_request
from utils.config import BASE_URL

def get_all_products():
    url = f"{BASE_URL}/products"
    return send_request("GET", url)
