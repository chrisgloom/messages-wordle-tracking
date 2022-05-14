from sheets.google_sheets import update
import unittest

from models.score_row import ScoreRow


class Test(unittest.TestCase):
    def test_sheet_score_row_parse(self):
        response = update([ScoreRow("2022-04-10 12:18:47", "1", "2", "3", "4", "5")])
        self.assertIsNotNone(response)
