from platformdirs import user_config_dir
from pathlib import Path


AUTH_URL = "https://allegro.pl/auth/oauth/authorize"
TOKEN_URL = "https://allegro.pl/auth/oauth/token"
APP_NAME = "allegro-auth"
TOKEN_FILE = Path(user_config_dir(APP_NAME)) / "tokens.json"

# Ensure the folder exists
TOKEN_FILE.parent.mkdir(parents=True, exist_ok=True)