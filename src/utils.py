import os

import settings


def run_server():
    os.system(f'uvicorn {settings.Path.app} --reload')
