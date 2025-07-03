import pytest
from unittest.mock import patch, MagicMock
from allegro_auth.client import AllegroAuth


@pytest.fixture
def auth():
    return AllegroAuth("client_id", "client_secret", "http://localhost")


@patch("allegro_auth.client.read_tokens")
@patch("allegro_auth.client.is_token_valid", return_value=True)
def test_authenticate_returns_token(mock_valid, mock_read, auth):
    mock_token = MagicMock()
    mock_token.access_token = "valid_token"
    mock_token.expires_in = 3600
    mock_token.date = "2025-01-01T00:00:00"
    mock_read.return_value = mock_token

    token = auth.authenticate()
    assert token == "valid_token"


@patch("allegro_auth.client.read_tokens")
@patch("allegro_auth.client.is_token_valid", return_value=False)
@patch("allegro_auth.client.AllegroAuth._AllegroAuth__refresh_token")
@patch("allegro_auth.client.write_tokens")
def test_authenticate_refresh_token(mock_write, mock_refresh, mock_valid, mock_read, auth):
    mock_read.return_value = MagicMock(refresh_token="test_refresh")
    mock_refresh.return_value = {"access_token": "refreshed_token"}

    token = auth.authenticate()
    assert token == "refreshed_token"


@patch("allegro_auth.client.read_tokens", return_value=None)
@patch("allegro_auth.client.AllegroAuth._AllegroAuth__get_authorization_code", return_value="abc123")
@patch("allegro_auth.client.AllegroAuth._AllegroAuth__get_token_by_code", return_value={"access_token": "new_token"})
@patch("allegro_auth.client.write_tokens")
def test_authenticate_get_code(mock_write, mock_get_token, mock_get_code, mock_read, auth):
    token = auth.authenticate()
    assert token == "new_token"
