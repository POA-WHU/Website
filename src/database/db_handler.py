from typing import Union, List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.logger import Logger
from src.database.models import Base, Topic, Passage


class DBHandler:
    def __init__(self, engine_url: str):
        self.logger = Logger(self.__class__.__name__)
        engine = create_engine(engine_url)
        self._Session = sessionmaker(bind=engine)
        self.session = self._Session()
        Base.metadata.create_all(engine)

    def insert(self, data: Union[Topic, Passage]):
        self.logger.debug(f'trying to insert new row: {data}')
        session = self._Session()
        session.add(data)
        session.commit()
        self.logger.debug(f'inserted new row: {data}')
        session.close()

    def query_topic(self, **kwargs) -> List[Topic]:
        self.logger.debug(f'started query on topics with attributes: {kwargs}')
        session = self._Session()
        ret = list()
        for i in session.query(Topic).filter_by(**kwargs):
            ret.append(i)
        session.expunge_all()
        session.close()
        self.logger.debug(f'query finished')
        return ret

    def query_passage(self, **kwargs) -> List[Passage]:
        self.logger.debug(f'started query on passages with attributes: {kwargs}')
        session = self._Session()
        ret = list()
        for i in session.query(Passage).filter_by(**kwargs):
            ret.append(i)
        session.expunge_all()
        session.close()
        self.logger.debug(f'query finished')
        return ret


if __name__ == '__main__':
    from src import settings
    db_h = DBHandler(settings.DBHandler.engine)
    print(db_h.query_topic(source='test'))
