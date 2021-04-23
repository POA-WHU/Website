from typing import Union
import os

import api
import database
import settings


def trans_model(item: Union[database.Topic, database.Passage]):
    if type(item) == database.Topic:
        return api.Topic(
            name=item.name,
            abstract=item.abstract,
            heat=item.heat,
            pnum=item.pnum,
            pic_url=item.pic_url,
        )
    elif type(item) == database.Passage:
        return api.Passage(
            title=item.title,
            abstract=item.abstract,
            website=item.website,
            date=item.date,
            url=item.url,
        )
    else:
        raise TypeError(f'got wrong type: {type(item)}')


def run_server():
    os.system(f'uvicorn {settings.Path.app} --reload')
