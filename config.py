from os import environ
from dotenv import load_dotenv
from os.path import join, dirname


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CLIENT_ID = environ.get('CLIENT_ID')
CLIENT_SECRET = environ.get('CLIENT_SECRET')
AUTH_URL = environ.get('AUTH_URL')
TOKEN_URL = environ.get('TOKEN_URL')
REDIRECT_URI = environ.get('REDIRECT_URI')
TOKEN_FILE = join(dirname(__file__), 'tokens.json')