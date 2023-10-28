import uvicorn
import sys
from pathlib import Path


if __name__ == '__main__':
    path = Path(__file__).resolve().parent.parent
    sys.path.insert(1, str(path))
    uvicorn.run("server.app:app", port=8001)
