from collections import defaultdict
from typing import List, Dict
from rng import Rng

from relics import RelicsManager


def group_relics_by_rarity_and_shuffle(relics: List[str], rng: Rng) -> Dict:
    relics_by_rarity = defaultdict(list)
    for relic in relics:
        rarity = RelicsManager.get_relic_rarity(relic)
        relics_by_rarity[rarity].append(relic)
    for rarity in relics_by_rarity.keys():
        rng.unstable_shuffle(relics_by_rarity[rarity])
    return relics_by_rarity

class RunManager:
    @staticmethod
    def populate_relics(run_state):
        locked_relics = run_state.progress.get_locked_relics()
        shared_relics = RelicsManager.get_shared_relics() - locked_relics
        character_relics = RelicsManager.get_character_relics(run_state.character) - locked_relics
        player_relics = shared_relics | character_relics

        run_state.shared_relic_grab_bag = group_relics_by_rarity_and_shuffle(shared_relics, run_state.rng_set.up_front)        
        run_state.player_relic_grab_bag = group_relics_by_rarity_and_shuffle(player_relics, run_state.rng_set.up_front)

    @staticmethod
    def generate_rooms(run_state):
        pass

    @staticmethod
    def enter_act(run_state, act_idx):
        pass
