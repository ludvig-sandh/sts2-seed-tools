from run_rng_set import RunRngSet
from unknown_map_point_odds import UnknownMapPointOdds
from progress import Progress
from character import Character

class RunState:
    def __init__(self, rng_set: RunRngSet, odds, progress: Progress, character: Character):
        self.rng_set = rng_set
        self.odds = odds
        self.progress = progress
        self.character = character
        
        self.shared_relic_grab_bag = dict()
        self.player_relic_grab_bag = dict()

    @staticmethod
    def create_for_new_run(seed: str, progress: Progress, character: Character):
        rng_set = RunRngSet(seed)
        odds = UnknownMapPointOdds(rng_set.unknown_map_point)
        run_state = RunState(rng_set, odds, progress, character)
        return run_state