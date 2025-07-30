def get_auth_headers(token: str = None):
    headers = {
        "X-Realm-ID": "dev-realm",
        "X-Appz-ID": "kiosk-self-ordering"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers
