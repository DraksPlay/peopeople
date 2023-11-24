from dotenv import load_dotenv
import os


load_dotenv()

"""
COMMON
"""
DEBUG = True

"""
API
"""
API_URL = "/api/v1"
API_PORT = 8000
API_HOST = "127.0.0.1"

"""
DATABASE
"""
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_URL_PROD = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@db:{DB_PORT}/{DB_NAME}"


DB_HOST_TEST = os.environ.get("DB_HOST_TEST")
DB_PORT_TEST = os.environ.get("DB_PORT_TEST")
DB_NAME_TEST = os.environ.get("DB_NAME_TEST")
DB_USER_TEST = os.environ.get("DB_USER_TEST")
DB_PASS_TEST = os.environ.get("DB_PASS_TEST")

DATABASE_URL_TEST = f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"


"""
SERVER
"""
SERVER_URL = "/api/v1"
SERVER_PORT = 8081
SERVER_HOST = "127.0.0.1"
