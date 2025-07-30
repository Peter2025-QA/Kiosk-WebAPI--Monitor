import requests
from utils.token_manager import get_auth_headers
from config.env_config import BASE_URL

def test_sign_in_with_phone():
    token = "your_token_here"  # Replace with a valid token
    headers = get_auth_headers(token)
    url = f"{BASE_URL}/v1/auth/sign-in-with-phone-numbe"
    params = {
        "merchant-id": "your_merchant_id",
        "location-id": "5382410a-d2d7-4271-a29c-385a38ebbca9"
    }
    payload = {
        "phone_number": "+13124029005",
        "verification_code": "684570"
    }
    response = requests.post(url, headers=headers, params=params, json=payload)
    print(response.status_code, response.json())
    assert response.status_code in [200, 401]
