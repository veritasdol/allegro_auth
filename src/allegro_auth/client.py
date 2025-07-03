import requests
from urllib.parse import urlencode
from .config import AUTH_URL, TOKEN_URL
from .token_manager import read_tokens, write_tokens, is_token_valid

requests.packages.urllib3.disable_warnings()

def send_request(method: str, url: str, data: dict):
    try:
        response = requests.request(
            method=method,
            url=url,
            data=data,
            auth=(CLIENT_ID, CLIENT_SECRET),
            verify=True,
            allow_redirects=False
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise SystemExit(f"Request failed: {e}")

def get_authorization_code():
    params = urlencode({
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI
    })
    print(f"Open this URL and authorize the app:\n\n{AUTH_URL}?{params}\n")
    return input("Enter the code from URL: ")

def get_token_by_code(code: str):
    return send_request("POST", TOKEN_URL, {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI
    })

def refresh_token(refresh_token: str):
    return send_request("POST", TOKEN_URL, {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "redirect_uri": REDIRECT_URI
    })

def authenticate(client_secret: str, client_id: str, redirect_uri: str) -> str:
    global CLIENT_ID
    global CLIENT_SECRET
    global REDIRECT_URI
    CLIENT_ID = client_id
    CLIENT_SECRET = client_secret
    REDIRECT_URI = redirect_uri

    token_data = read_tokens()

    if token_data and is_token_valid(token_data.expires_in, token_data.date):
        return token_data.access_token

    if token_data:
        new_tokens = refresh_token(token_data.refresh_token)
    else:
        code = get_authorization_code()
        new_tokens = get_token_by_code(code)

    write_tokens(new_tokens)
    return new_tokens["access_token"]
