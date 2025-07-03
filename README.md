[![PyPI version](https://img.shields.io/pypi/v/allegro_auth?color=blue)](https://pypi.org/project/allegro_auth/)
[![Python version](https://img.shields.io/pypi/pyversions/allegro_auth)](https://pypi.org/project/allegro_auth/)
[![License](https://img.shields.io/github/license/veritasdol/allegro_auth)](https://github.com/veritasdol/allegro_auth/blob/main/LICENSE)
[![Tests](https://github.com/veritasdol/allegro_auth/actions/workflows/tests.yml/badge.svg)](https://github.com/veritasdol/allegro_auth/actions/workflows/tests.yml)

# Allegro OAuth2 Authenticator

A lightweight Python package for handling OAuth2 authentication with the Allegro API.

## Features

- Gets authorization code from Allegro
- Exchanges code for access and refresh tokens
- Automatically refreshes expired access tokens
- Validates tokens with Pydantic
- Stores tokens in `tokens.json`

## Requirements

- Python 3.9+
- Allegro developer account

## Installation

```bash
pip install allegro_auth
```

## Example Usage

```python
from allegro_auth import AllegroAuth


allegro = AllegroAuth(
   client_id="your_client_id",
   client_secret="your_client_secret",
   redirect_uri="your_redirect_uri"
   )

token = allegro.authenticate()
```

On first run, you'll be prompted to open a URL and paste the authorization code.

## Token Storage

Tokens are stored in a local `tokens.json` file and automatically refreshed when expired.
Location follows OS conventions via `platformdirs`:

## License

This project is licensed under the MIT License.

## Links

* [Allegro API Docs](https://developer.allegro.pl/)

* [Project Homepage](https://github.com/veritasdol/allegro_auth)

* [Issue Tracker](https://github.com/veritasdol/allegro_auth/issues)
