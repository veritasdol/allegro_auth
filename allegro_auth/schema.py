from pydantic import BaseModel

class TokenSchema(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str
    expires_in: int
    scope: str
    allegro_api: bool
    iss: str
    jti: str
    date: str