from datetime import datetime

from logger import Logger
from utils import run_server

if __name__ == '__main__':
    logger = Logger('main')
    logger.info(f'server started running at {datetime.now()}')
    run_server()
    logger.info(f'server terminated at {datetime.now()}')
