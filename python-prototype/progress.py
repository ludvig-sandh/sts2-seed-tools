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
    def __init__(self):
        self.discovered_acts = set()
        self.discovered_relics = set()
        self.discovered_epochs = set()
        self.discovered_potions = set()

    def discover_act(self, act: Act):
        self.discovered_acts.add(act)

    def discover_relic(self, relic):
        self.discovered_relics.add(relic)

    def discover_epoch(self, epoch):
        self.discovered_epochs.add(epoch)

    def discover_potion(self, potion):
        self.discovered_potions.add(potion)