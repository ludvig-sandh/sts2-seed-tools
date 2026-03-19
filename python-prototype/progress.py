from enum import Enum

class Act(Enum):
    OVERGROWTH = 0
    HIVE = 1
    GLORY = 2
    UNDERDOCKS = 3

    @staticmethod
    def create_from_name(name):
        NAME_TO_ACT_MAP = {
            "ACT.OVERGROWTH": Act.OVERGROWTH,
            "ACT.HIVE": Act.HIVE,
            "ACT.GLORY": Act.GLORY,
            "ACT.UNDERDOCKS": Act.UNDERDOCKS
        }
        try:
            return NAME_TO_ACT_MAP[name]
        except LookupError:
            raise ValueError(f"An act with name {name} doesn't exist.")

class Progress:
    # Default progress for a new save
    def __init__(self):
        self.unlocked_acts = set([Act.OVERGROWTH, Act.HIVE, Act.GLORY])

    def unlock_act(self, act: Act):
        self.unlocked_acts.add(act)