from collections import defaultdict
from typing import List, Dict
from rng import Rng
from event import EventDB
from relics import RelicsManager
from encounter import EncounterDB
from act import ActHelper

from dataclasses import dataclass


@dataclass
class BagItem:
    item: object
    weight: float


def group_relics_by_rarity_and_shuffle(relics: List[str], rng: Rng) -> Dict:
    relics_by_rarity = defaultdict(list)
    for relic in relics:
        rarity = RelicsManager.get_relic_rarity(relic)
        relics_by_rarity[rarity].append(relic)
    for rarity in relics_by_rarity:
        relics_by_rarity[rarity] = rng.unstable_shuffle(relics_by_rarity[rarity])
    return relics_by_rarity

def total_weight(grab_bag):
    return sum(element.weight for element in grab_bag)

def grab_index(grab_bag, rng: Rng) -> int:
    num = rng.next_double() * total_weight(grab_bag)
    num2 = 0.0
    for i in range(len(grab_bag)):
        num2 += grab_bag[i].weight
        if num < num2:
            return i
    return -1

def grab_index_with_predicate(grab_bag, rng, predicate = None) -> int:
    if predicate is not None:
        fulfills_pred = map(predicate, grab_bag)
        none_fulfills = not any(fulfills_pred)
        if none_fulfills:
            return -1
        
    num = grab_index(grab_bag, rng)
    while (predicate is not None and num >= 0 and not predicate(grab_bag[num])):
        num = grab_index(grab_bag, rng)

    return num

def grab_and_remove(grab_bag, rng, predicate = None):
    num = grab_index_with_predicate(grab_bag, rng, predicate)
    if num < 0:
        return None
    item = grab_bag[num].item
    del grab_bag[num]
    return item

def last_or_none(li: list):
    if len(li):
        return li[-1]
    return None

def shares_tag(enc1, enc2) -> bool:
    if enc2 is None:
        return False
    
    tags1 = EncounterDB.get_metadata_for_encounter(enc1).tags
    tags2 = EncounterDB.get_metadata_for_encounter(enc2).tags
    return bool(set(tags1) & set(tags2))

def add_without_repeating_tags(encounter_list, grab_bag, rng):
    encounter = grab_and_remove(
        grab_bag,
        rng,
        lambda bag_item: (
            not shares_tag(bag_item.item, last_or_none(encounter_list))
            and bag_item.item != last_or_none(encounter_list)
        )
    )

    if encounter is None:
        encounter = grab_and_remove(grab_bag, rng)

    if encounter is not None:
        encounter_list.append(encounter)

class RunManager:
    @staticmethod
    def populate_relics(run_state):
        locked_relics = run_state.progress.get_locked_relics()
        shared_relics = [r for r in RelicsManager.get_shared_relics() if r not in locked_relics]
        character_relics = [r for r in RelicsManager.get_character_relics(run_state.character) if r not in locked_relics]
        player_relics = shared_relics + character_relics
        rarities_to_keep = [RelicsManager.RelicRarity.COMMON, RelicsManager.RelicRarity.UNCOMMON, RelicsManager.RelicRarity.RARE, RelicsManager.RelicRarity.SHOP]
        player_relics = [r for r in player_relics if RelicsManager.get_relic_rarity(r) in rarities_to_keep]

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
            count = run_state.rng_set.up_front.next_int(len(shared_ancient_events) + 1)
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

            normal_encounters = []
            elite_encounters = []

            grab_bag = []
            num_weak_encounters = ActHelper.get_num_weak_encounters(act)
            for _ in range(num_weak_encounters):
                if len(grab_bag) == 0:
                    for weak_encounter in EncounterDB.get_weak_encounters(act):
                        grab_bag.append(BagItem(weak_encounter, 1.0))
                add_without_repeating_tags(normal_encounters, grab_bag, run_state.rng_set.up_front)
                
            grab_bag2 = []
            for _ in range(num_weak_encounters, ActHelper.get_num_rooms(act)):
                if len(grab_bag2) == 0:
                    for regular_encounter in EncounterDB.get_regular_encounters(act):
                        grab_bag2.append(BagItem(regular_encounter, 1.0))
                add_without_repeating_tags(normal_encounters, grab_bag2, run_state.rng_set.up_front)
                
            grab_bag3 = []
            for _ in range(15):
                if len(grab_bag3) == 0:
                    for elite_encounter in EncounterDB.get_elite_encounters(act):
                        grab_bag3.append(BagItem(elite_encounter, 1.0))
                add_without_repeating_tags(elite_encounters, grab_bag3, run_state.rng_set.up_front)

            run_state.set_normal_encounters_for_act(act, normal_encounters)
            run_state.set_elite_encounters_for_act(act, elite_encounters)

            all_boss_encounters = EncounterDB.get_boss_encounters(act)
            run_state.set_boss_for_act(act, run_state.rng_set.up_front.next_item(all_boss_encounters))

            ancients = ActHelper.get_ancients(act)
            locked_ancients = run_state.progress.get_locked_ancients()
            unlocked_ancients = [ancient for ancient in ancients if ancient not in locked_ancients]
            all_ancients = unlocked_ancients + run_state.shared_ancient_subsets_per_act[act]
            run_state.set_ancient_for_act(act, run_state.rng_set.up_front.next_item(all_ancients))


    @staticmethod
    def enter_act(run_state, act_idx):
        pass
