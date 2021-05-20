import pandas as pd
from tqdm import tqdm

from src import settings
from src.database.db_handler import DBHandler
from src.database.models import Passage


SRC_FILE = settings.Path.data / 'think_tank_clust.xlsx'


df = pd.read_excel(SRC_FILE)
handler = DBHandler(settings.DBHandler.engine)

handler.logger.disabled = True

for _, row in tqdm(df.iterrows()):
    handler.insert(
        Passage(
            title=row['title'],
            abstract=row['abstract'],
            website=row['group'],
            date=row['date'].to_pydatetime().date(),
            url=row['url'],
            topic=row['clusted_label']
        )
    )
