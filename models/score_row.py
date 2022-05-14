from dataclasses import dataclass
from typing import Optional, List
from Config import WordleConfig


@dataclass
class ScoreRow:
    date: str
    malcolm: Optional[str] = None
    travis: Optional[str] = None
    chris: Optional[str] = None
    dylan: Optional[str] = None
    niky: Optional[str] = None

    def __init__(self, names: List[str], date) -> None:
        self.date = date
        name_dict = {}
        for name in names:
            name_dict[name] = None
        self.names = name_dict
        self.name_list = names

    def to_array(self):
        build_arr = [self.date]
        for name in self.name_list:
            build_arr.append(self.names[name])
        return build_arr

    def insert_score(self, name: str, score: str):
        if name in self.name_list:
            self.names[name] = score
