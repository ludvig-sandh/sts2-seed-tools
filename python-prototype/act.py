from rng import Rng
from util import get_deterministic_hash_code

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
        

class ActGenerator:
    DEFAULT_ACT_LIST = [Act.OVERGROWTH, Act.HIVE, Act.GLORY]

    @staticmethod
    def generate_act_list(seed: str, progress):
        acts = ActGenerator.DEFAULT_ACT_LIST
        rng = Rng(get_deterministic_hash_code(seed))
        
        if progress.is_epoch_discovered("UNDERDOCKS_EPOCH"):
            has_discovered_underdocks = progress.is_act_discovered(Act.UNDERDOCKS)

            # If underdocks was just discovered, force it. Otherwise 50/50
            if not has_discovered_underdocks or rng.next_bool():
                acts[0] = Act.UNDERDOCKS

        return acts