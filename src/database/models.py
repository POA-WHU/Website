from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.dialects.sqlite import INTEGER, TEXT

Base = declarative_base()


class Topic(Base):
    __tablename__ = 'topics'
    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT)
    year = Column(INTEGER)
    quarter = Column(INTEGER)
    heat = Column(INTEGER)
    p_num = Column(INTEGER)
    abstract = Column(TEXT)
    pic_url = Column(TEXT)
    source = Column(TEXT)

    def __repr__(self):
        return f'Topic<name={self.name}>'


class Passage(Base):
    __tablename__ = 'passages'
    id = Column(INTEGER, primary_key=True)
    title = Column(TEXT)
    date = Column(TEXT)
    content = Column(TEXT)
    abstract = Column(TEXT)
    website = Column(TEXT)
    url = Column(TEXT)
    topic = Column(TEXT)
    source = Column(TEXT)

    def __repr__(self):
        return f'Passage<name={self.title}>'
