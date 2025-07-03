import requests
from urllib.parse import urlencode
from .config import AUTH_URL, TOKEN_URL
from .token_manager import read_tokens, write_tokens, is_token_valid

requests.packages.urllib3.disable_warnings()


class AllegroAuth:
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def __send_request(self, method: str, data: dict):
        try:
            response = requests.request(
                method=method,
                url=TOKEN_URL,
                data=data,
                auth=(self.client_id, self.client_secret),
                verify=True,
                allow_redirects=False
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise SystemExit(f"Request failed: {e}")

    def __get_authorization_code(self):
        params = urlencode({
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri
        })
        print(f"Open this URL and authorize the app:\n\n{AUTH_URL}?{params}\n")
        return input("Enter the code from URL: ")

    def __get_token_by_code(self, code: str):
        return self.__send_request(
            "POST",
            {
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": self.redirect_uri
            })

    def __refresh_token(self, refresh_token: str):
        return self.__send_request(
            "POST",
            {
                "grant_type": "refresh_token",
                "refresh_token": refresh_token,
                "redirect_uri": self.redirect_uri
            })

    def authenticate(self) -> str:

        token_data = read_tokens()

        if token_data and is_token_valid(token_data.expires_in, token_data.date):
            return token_data.access_token

        if token_data:
            new_tokens = self.__refresh_token(token_data.refresh_token)
        else:
            code = self.__get_authorization_code()
            new_tokens = self.__get_token_by_code(code)

        write_tokens(new_tokens)
        return new_tokens["access_token"]
