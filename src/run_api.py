import uvicorn
import sys
from pathlib import Path

from config import API_HOST, API_PORT


if __name__ == '__main__':
    path = Path(__file__).resolve().parent.parent
    sys.path.insert(1, str(path))
    uvicorn.run("api.app:app", host=API_HOST, port=API_PORT)
