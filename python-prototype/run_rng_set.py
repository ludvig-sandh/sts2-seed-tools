from util import get_deterministic_hash_code
from rng import Rng

class RunRngSet:
    def __init__(self, string_seed: str):
        self.string_seed = string_seed
        self.seed = get_deterministic_hash_code(string_seed)
        self.up_front = Rng(self.seed, "up_front")
        self.shuffle = Rng(self.seed, "shuffle")
        self.unknown_map_point = Rng(self.seed, "unknown_map_point")
        self.combad_card_generation = Rng(self.seed, "combad_card_generation")
        self.combat_potion_generation = Rng(self.seed, "combat_potion_generation")
        self.combat_card_selection = Rng(self.seed, "combat_card_selection")
        self.combat_energy_costs = Rng(self.seed, "combat_energy_costs")
        self.combat_targets = Rng(self.seed, "combat_targets")
        self.monster_ai = Rng(self.seed, "monster_ai")
        self.niche = Rng(self.seed, "niche")
        self.combat_orbs = Rng(self.seed, "combat_orbs")
        self.treasure_room_relic = Rng(self.seed, "treasure_room_relic")
