import json
from datetime import datetime, timedelta
from unittest.mock import patch, mock_open
from allegro_auth.token_manager import (
    is_token_valid,
    read_tokens,
    write_tokens
)
from allegro_auth.schema import TokenSchema


def test_is_token_valid_true():
    now = datetime.now()
    date = (now - timedelta(seconds=10)).isoformat()
    assert is_token_valid(3600, date) is True

def test_is_token_valid_false():
    past = datetime.now() - timedelta(hours=2)
    date = past.isoformat()
    assert is_token_valid(3600, date) is False


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps({
    "access_token": "abc",
    "token_type": "bearer",
    "refresh_token": "xyz",
    "expires_in": 3600,
    "scope": "allegro:all",
    "allegro_api": True,
    "iss": "allegro",
    "jti": "token-id",
    "date": datetime.now().isoformat()
}))
@patch("allegro_auth.token_manager.TOKEN_FILE", "dummy_path.json")
def test_read_tokens_valid(mock_file):
    token = read_tokens()
    assert isinstance(token, TokenSchema)
    assert token.access_token == "abc"


@patch("builtins.open", side_effect=FileNotFoundError)
@patch("allegro_auth.token_manager.TOKEN_FILE", "dummy_path.json")
def test_read_tokens_file_not_found(mock_file):
    assert read_tokens() is None


@patch("builtins.open", new_callable=mock_open)
@patch("allegro_auth.token_manager.TOKEN_FILE", "dummy_path.json")
@patch("allegro_auth.token_manager.datetime")
def test_write_tokens(mock_datetime, mock_file):
    mock_datetime.now.return_value = datetime(2025, 1, 1, 12, 0, 0)
    
    tokens = {
        "access_token": "abc",
        "token_type": "bearer",
        "refresh_token": "xyz",
        "expires_in": 3600,
        "scope": "allegro:all",
        "allegro_api": True,
        "iss": "allegro",
        "jti": "token-id"
    }

    write_tokens(tokens)

    written_data = "".join(call.args[0] for call in mock_file().write.call_args_list)
    result = json.loads(written_data)

    assert result["access_token"] == "abc"
    assert result["date"] == "2025-01-01T12:00:00"

