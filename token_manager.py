import json
from datetime import datetime, timedelta
from typing import Optional
from schema import TokenSchema
from config import TOKEN_FILE

def is_token_valid(expires_in: int, date: str) -> bool:
    token_time = datetime.fromisoformat(date)
    return (token_time + timedelta(seconds=expires_in)) > datetime.now()

def read_tokens() -> Optional[TokenSchema]:
    try:
        with open(TOKEN_FILE, 'r') as f:
            data = json.load(f)
            return TokenSchema(**data)
    except (json.JSONDecodeError, FileNotFoundError, ValueError):
        return None

def write_tokens(tokens: dict):
    tokens['date'] = datetime.now().isoformat()
    with open(TOKEN_FILE, 'w') as f:
        json.dump(tokens, f, indent=2)