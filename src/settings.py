import pathlib
import logging


class Path:
    src = pathlib.Path(__file__).absolute().parent
    project = src.parent
    data = project / 'data'
    app = 'api.app:app'


class Logger:
    format = '[%(name)-10s] %(levelname)-8s: %(message)s'
    level = logging.DEBUG


class DBHandler:
    engine = f'sqlite:///{Path.project}\\db.sqlite3'


class App:
    class CORS:
        origins = ['*']
        credentials = True
        methods = ['*']
        headers = ['*']
