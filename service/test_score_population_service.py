from service.score_population_service import extract_score
import unittest


class Test(unittest.TestCase):
    def test_multiline(self):
        wordle_string = """
            one of those words
            
            Wordle 259 6/6
            
            β¬β¬β¬π¨π©
            π¨β¬β¬β¬π©
            β¬π©π©β¬π©
            β¬π©π©β¬π©
            β¬π©π©β¬π©
            π©π©π©π©π©
            
            very fucking close lol
        """
        score = extract_score(wordle_string)
        self.assertIs(score, '6')

    def test_ignore_tapbacks(self):
        wordle_string = """
            Emphasized βWordle 259 2/6

            β¬β¬β¬π¨π¨
            π©π©π©π©π©
            β
        """
        score = extract_score(wordle_string)
        self.assertIs(score, None)


    def test_no_middle_number(self):
        wordle_string = """
            Emphasized wordle  2/6

            β¬β¬β¬π¨π¨
            π©π©π©π©π©
            
        """
        score = extract_score(wordle_string)
        self.assertIs(score, None)
