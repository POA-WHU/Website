import pickle
import os

from tqdm import tqdm

from src import settings
from src.database.db_handler import DBHandler
from src.database.models import Passage, Topic

handler = DBHandler(settings.DBHandler.engine)
