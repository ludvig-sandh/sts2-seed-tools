from run_rng_set import RunRngSet
from unknown_map_point_odds import UnknownMapPointOdds

class RunState:
    def __init__(self, rng_set, odds):
        self.rng_set = rng_set
        self.odds = odds

    @staticmethod
    def create_for_new_run(seed: str):
        rng_set = RunRngSet(seed)
        odds = UnknownMapPointOdds(rng_set.unknown_map_point)
        run_state = RunState(rng_set, odds)
        return run_state