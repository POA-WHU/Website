from pydantic import BaseModel


class Topic(BaseModel):
    name: str
    abstract: str
    heat: int
    pnum: int
    pic_url: str


class Passage(BaseModel):
    title: str
    abstract: str
    website: str
    date: str
    url: str


if __name__ == '__main__':
    print(dir(Topic))