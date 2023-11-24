import uvicorn
import sys
from pathlib import Path

from config import SERVER_HOST, SERVER_PORT


if __name__ == '__main__':
    path = Path(__file__).resolve().parent.parent
    sys.path.insert(1, str(path))
    uvicorn.run("server.app:app", host=SERVER_HOST, port=SERVER_PORT)
