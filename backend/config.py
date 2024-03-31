import os
from dotenv import load_dotenv


load_dotenv()


# DOCKER
DOCKER = int(os.environ.get("DOCKER", 0))


# DATABASE
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{'db' if DOCKER else f'{DB_HOST}:{DB_PORT}'}/{DB_NAME}"

# API
API_HOST = "localhost"
API_PORT = 8000
API_URL = f"http://{API_HOST}:{API_PORT}"

# SECRET KEYS
AUTH_SECRET_KEY = os.environ.get("AUTH_SECRET_KEY")
