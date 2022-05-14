import re
from typing import Optional

import Config
from db.chat_history import get_total_chat_history
from datetime import datetime, timedelta
from models.score_row import ScoreRow


NUMBER_TO_NAME = Config.WordleConfig.USER_PHONE_NUMS_TO_NAME


# initialize dates for populating
def init_data_for_date(date: datetime.date):
    working_list_data = {}
    while date != datetime.today().date():
        date = date + timedelta(days=1)
        working_list_data[date] = ScoreRow(date=date.isoformat(), names=Config.WordleConfig.USERS)
    return working_list_data


def extract_score(wordle: str) -> Optional[str]:
    # weird voodoo in the regex is negative lookbehind
    # aka we assert there is not a quote directly before the score, this prevents us
    # registering tapbacks as a legit score...mostly
    if "“" in wordle:
        return
    maybe_match = re.search("(?<!“)Wordle \d+ (\d|X)/\d", wordle)
    if maybe_match is not None:
        return maybe_match.groups()[0]
    else:
        return


# take a score row object and enrich it before returning it to the dict
def populate_found_data(score_row: ScoreRow, who: str, score: str) -> ScoreRow:
    score_row.insert_score(who, score)
    return score_row


def populate(start_date: datetime.date = None):
    rows = get_total_chat_history()
    if not start_date:
        start_date = datetime.fromisoformat(rows[0][2]).date()
    score_dict = init_data_for_date(start_date)
    for row in rows:
        if row[0]:
            maybe_score = extract_score(row[0])
            if maybe_score:
                date = datetime.fromisoformat(row[2]).date()
                if date in score_dict:
                    score_row = populate_found_data(
                        score_dict[date],
                        NUMBER_TO_NAME.get(row[1]),
                        maybe_score)
                    score_dict[date] = score_row
    return score_dict


if __name__ == '__main__':
    result = populate(datetime.fromisoformat("2022-01-10").date())
    print(result)
