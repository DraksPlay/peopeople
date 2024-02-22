import uvicorn


if __name__ == '__main__':
    uvicorn.run("web.app:app", host="localhost", port=8001)