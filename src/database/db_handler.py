from typing import Union

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

    def query_topic(self, source: str, year: int, quarter: int) -> list[Topic]:
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

    def query_passage(self, topic: str) -> list[Passage]:
        self.logger.debug(f'started query on passages with attributes: {topic}')
        session = self._Session()
        ret = list()
        for i in session.query(Passage).filter_by(topic=topic):
            ret.append(i)
        session.expunge_all()
        session.close()
        self.logger.debug(f'query finished')
        return ret


if __name__ == '__main__':
    import settings

    dbh = DBHandler(settings.DBHandler.engine)
    print(dbh.query_topic('test_1', 2000, 1))
    print(dbh.query_passage('test_1'))
    # dbh.insert(
    #     Topic(
    #         name='test_0',
    #         year=2000,
    #         quarter=1,
    #         heat=100,
    #         pnum=10,
    #         abstract='test_0',
    #         pic_url='test_0.com',
    #         source='test_0'
    #     )
    # )
    # dbh.insert(
    #     Passage(
    #         title='test_0',
    #         abstract='test_0',
    #         website='test_0.com',
    #         date='2000-01-01',
    #         url='test_0.com/test_0',
    #         topic='test_0'
    #     )
    # )
