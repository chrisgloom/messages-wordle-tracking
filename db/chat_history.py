import sqlite3
from contextlib import closing

import Config

db_path = Config.WordleConfig.PATH_TO_LOCAL_CHAT_DB

# the weird addition is because apple doesn't start at unixepoch, division is because of milliseconds
sql = f"""
        select 
            text ,
            h.id,
            datetime((m.date / 1000000000) + 978307200, 'unixepoch', 'localtime') as TextDate 
        from message m 
        left join handle h on h.ROWID = m.handle_id
        where cache_roomnames = '{Config.WordleConfig.CACHE_ROOMNAMES_GROUPCHAT}'
"""


def get_total_chat_history():
    with closing(sqlite3.connect(db_path)) as connection:
        with closing(connection.cursor()) as cursor:
            return cursor.execute(sql).fetchall()


if __name__ == '__main__':
    rows = get_total_chat_history()
    # check if this is even a wordle if not discard
    # wordle found, who's it from?
    print(rows)

