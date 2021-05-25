import pandas as pd
from tqdm import tqdm

from src import settings
from src.database.db_handler import DBHandler
from src.database.models import Passage, Topic

SRC_FILE = settings.Path.data / 'think_tank_clust.xlsx'
SOURCE = 'think_tank'

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
            content = row['content'],
            url=row['url'],
            topic=row['clusted_label'],
            source=SOURCE
        )
    )
    # try:
    #     handler.insert(
    #         Topic(
    #             name=row['name'],
    #             year=row['year'][1: 5],
    #             quarter=row['quarter'],
    #             heat=row['heat'],
    #             p_num=row['p_num'],
    #             abstract=row['abstract'],
    #             pic_url=None,
    #             source=row['source']
    #         )
    #     )
    # except TypeError:
    #     handler.insert(
    #         Topic(
    #             name=row['name'],
    #             year=row['year'],
    #             quarter=row['quarter'],
    #             heat=row['heat'],
    #             p_num=row['p_num'],
    #             abstract=row['abstract'],
    #             pic_url=None,
    #             source=row['source']
    #         )
    #     )