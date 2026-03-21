from collections import defaultdict
from typing import List, Dict
from rng import Rng
from event import EventDB

from relics import RelicsManager


def group_relics_by_rarity_and_shuffle(relics: List[str], rng: Rng) -> Dict:
    relics_by_rarity = defaultdict(list)
    for relic in relics:
        rarity = RelicsManager.get_relic_rarity(relic)
        relics_by_rarity[rarity].append(relic)
    for rarity in relics_by_rarity.keys():
        relics_by_rarity[rarity] = rng.unstable_shuffle(relics_by_rarity[rarity])
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
        shared_ancient_events = []
        if run_state.progress.is_epoch_discovered("DARV_EPOCH"):
            shared_ancient_events.append("DARV")

        run_state.rng_set.up_front.unstable_shuffle(shared_ancient_events)

        run_state.shared_ancient_subsets_per_act = defaultdict(list)
        for act in run_state.acts[1:]:
            count = run_state.rng_set.up_front.next_int(len(shared_ancient_events))
            run_state.shared_ancient_subsets_per_act[act] = shared_ancient_events[:count]
            shared_ancient_events = shared_ancient_events[count:]

        for i in range(len(run_state.acts)):
            act = run_state.acts[i]
            all_events = EventDB.get_events_for_act(act) + EventDB.get_shared_events()

            # Remove locked events
            events_to_remove = []
            if not run_state.progress.is_epoch_discovered("EVENT1_EPOCH"):
                events_to_remove.append("TrashHeap")
            if not run_state.progress.is_epoch_discovered("EVENT2_EPOCH"):
                events_to_remove.append("Reflections")
            if not run_state.progress.is_epoch_discovered("EVENT3_EPOCH"):
                events_to_remove.append("ColorfulPhilosophers")
            events = [event for event in all_events if event not in events_to_remove]
            
            events = run_state.rng_set.up_front.unstable_shuffle(events)
            run_state.set_room_events_for_act(act, events)


    @staticmethod
    def enter_act(run_state, act_idx):
        pass
