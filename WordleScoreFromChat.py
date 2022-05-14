import Config
from service import score_population_service
from sheets import google_sheets
from datetime import datetime


def main():
    score_objects = score_population_service.populate(datetime.fromisoformat(Config.WordleConfig.FROM_DATE).date())
    score_list = list(score_objects.values())
    response = google_sheets.update(score_list)
    print(response)


if __name__ == '__main__':
    main()
