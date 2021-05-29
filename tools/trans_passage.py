import pickle
import os

from tqdm import tqdm

from src import settings
from src.database.db_handler import DBHandler
from src.database.models import Passage, Topic

handler = DBHandler(settings.DBHandler.engine)


session = handler._Session()
passages = session.query(Passage).filter_by()

for i in passages:
    date = i.date
    i.year = int(date[:4])
    month = int(date[5:7])
    i.quarter = (month - 1) // 3 + 1

session.commit()
session.close()
