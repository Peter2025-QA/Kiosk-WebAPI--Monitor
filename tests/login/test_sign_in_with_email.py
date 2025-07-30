import requests
from utils.token_manager import get_auth_headers
from config.env_config import BASE_URL

def test_sign_in_with_email():
    url = f"{BASE_URL}/v1/auth/sign-in-with-email"
    payload = {
        "email": "test002@infi.us",
        "password": "123123"
    }
    headers = get_auth_headers()
    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code, response.json())
    assert response.status_code in [200, 401]
