from run_rng_set import RunRngSet
from unknown_map_point_odds import UnknownMapPointOdds
from progress import Progress
from character import Character
from act import Act

from typing import List


class RunState:
    def __init__(self, rng_set: RunRngSet, odds, progress: Progress, acts: List["Act"], character: Character):
        self.rng_set = rng_set
        self.odds = odds
        self.progress = progress
        self.acts = acts
        self.character = character
        
        self.shared_relic_grab_bag = dict()
        self.player_relic_grab_bag = dict()

        self.room_events_per_act = dict()
        self.normal_encounters_per_act = dict()
        self.elite_encounters_per_act = dict()
        self.boss_per_act = dict()
        self.ancient_per_act = dict()

    @staticmethod
    def create_for_new_run(seed: str, progress: Progress, acts: List["Act"], character: Character):
        rng_set = RunRngSet(seed)
        odds = UnknownMapPointOdds(rng_set.unknown_map_point)
        run_state = RunState(rng_set, odds, progress, acts, character)
        return run_state
    
    def set_room_events_for_act(self, act, events):
        self.room_events_per_act[act] = events

    def set_normal_encounters_for_act(self, act, encounters):
        self.normal_encounters_per_act[act] = encounters

    def set_elite_encounters_for_act(self, act, encounters):
        self.elite_encounters_per_act[act] = encounters

    def set_boss_for_act(self, act, boss):
        self.boss_per_act[act] = boss

    def set_ancient_for_act(self, act, ancient):
        self.ancient_per_act[act] = ancient