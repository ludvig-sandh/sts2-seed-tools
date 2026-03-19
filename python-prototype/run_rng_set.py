from util import get_deterministic_hash_code
from rng import Rng

class RunRngSet:
    def __init__(self, string_seed: str):
        self.string_seed = string_seed
        self.seed = get_deterministic_hash_code(string_seed)
        self.up_front = Rng(self.seed, "up_front")
        self.Shuffle = Rng(self.seed, "shuffle")
        self.UnknownMapPoint = Rng(self.seed, "unknown_map_point")
        self.CombatCardGeneration = Rng(self.seed, "combad_card_generation")
        self.CombatPotionGeneration = Rng(self.seed, "combat_potion_generation")
        self.CombatCardSelection = Rng(self.seed, "combat_card_selection")
        self.CombatEnergyCosts = Rng(self.seed, "combat_energy_costs")
        self.CombatTargets = Rng(self.seed, "combat_targets")
        self.MonsterAi = Rng(self.seed, "monster_ai")
        self.Niche = Rng(self.seed, "niche")
        self.CombatOrbs = Rng(self.seed, "combat_orbs")
        self.TreasureRoomRelic = Rng(self.seed, "treasure_room_relic")
