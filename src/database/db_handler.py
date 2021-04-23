from typing import Union, List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from logger import Logger
from database.models import Base, Topic, Passage


class DBHandler:
    def __init__(self, engine_url: str):
        self.logger = Logger(self.__class__.__name__)
        engine = create_engine(engine_url)
        self._Session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)

    def insert(self, data: Union[Topic, Passage]):
        self.logger.debug(f'trying to insert new row: {data}')
        session = self._Session()
        session.add(data)
        session.commit()
        self.logger.debug(f'inserted new row: {data}')
        session.close()

    def query_topic(self, source: str, year: int, quarter: int) -> List[Topic]:
        self.logger.debug(f'started query on topics with attributes: {source, year, quarter}')
        session = self._Session()
        ret = list()
        for i in session.query(Topic).filter_by(
            source=source,
            year=year,
            quarter=quarter
        ):
            ret.append(i)
        session.expunge_all()
        session.close()
        self.logger.debug(f'query finished')
        return ret

    def query_passage(self, topic: str) -> List[Passage]:
        self.logger.debug(f'started query on passages with attributes: {topic}')
        session = self._Session()
        ret = list()
        for i in session.query(Passage).filter_by(topic=topic):
            ret.append(i)
        session.expunge_all()
        session.close()
        self.logger.debug(f'query finished')
        return ret
