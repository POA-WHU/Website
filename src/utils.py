import uvicorn

from app import app


def run_server():
    uvicorn.run(app)
