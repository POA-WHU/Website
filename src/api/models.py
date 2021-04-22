from pydantic import BaseModel


class Topic(BaseModel):
    name: str
    abstract: str
    year: int
    quarter: int
    heat: int
    pnum: int
    pic_url: str
    source: str


class Passage(BaseModel):
    title: str
    abstract: str
    website: str
    date: str
    url: str
    topic: str


if __name__ == '__main__':
    print(dir(Topic))