# Allegro OAuth2 Authenticator

This Python package handles authentication with the Allegro API using OAuth2.

## Features

- Gets authorization code from Allegro
- Exchanges code for access and refresh tokens
- Automatically refreshes expired access tokens
- Validates tokens with Pydantic
- Stores tokens in `tokens.json`

## Requirements

- Python 3.8+
- Allegro developer account
