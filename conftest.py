import pytest
from api.auth_api import login

@pytest.fixture(scope="session")
def auth_token():
    response = login("admin123", "admin123")
    token = response.json().get("token")
    return token
