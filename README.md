# Allegro OAuth2 Authenticator

This Python script handles authentication with the Allegro API using OAuth2.


## Features

- Gets authorization code from Allegro
- Exchanges code for access and refresh tokens
- Automatically refreshes expired access tokens
- Validates tokens with Pydantic
- Stores tokens in `tokens.json`
- Reads credentials from `.env` file


## Requirements

- Python 3.8+
- Allegro developer account


## Structure

```apache
allegro_auth/
├── config.py        # handles env loading
├── schema.py        # pydantic models
├── token_manager.py # token reading/writing/refreshing
├── client.py        # logic to authenticate and send requests
└── main.py          # entry point
```

## Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/allegro_auth.git
   cd allegro_auth
   ```
2. Create `.env` based on the example:

   ```bash
   cp .env.example .env
   ```
3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
4. Run the script:

   ```
   python auth.py
   ```


## Environment Variables

These variables are required and must be set in a `.env` file located in the root of the project.

Example `.env`:

```bash
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here
AUTH_URL=https://allegro.pl/auth/oauth/authorize
TOKEN_URL=https://allegro.pl/auth/oauth/token
REDIRECT_URI=http://localhost
```


| Variable          | Required | Description                                                    |
| ----------------- | -------- | -------------------------------------------------------------- |
| `CLIENT_ID`     | ✅       | Client ID from your Allegro Developer application              |
| `CLIENT_SECRET` | ✅       | Client secret from your Allegro Developer application          |
| `AUTH_URL`      | ✅       | Authorization endpoint, usually `https://.../authorize`      |
| `TOKEN_URL`     | ✅       | Token endpoint, usually `https://.../token`                  |
| `REDIRECT_URI`  | ✅       | Redirect URI registered in your app (e.g.`http://localhost`) |

> ⚠️ Do **not** commit your real `.env` file — add it to `.gitignore`.

## License
MIT
