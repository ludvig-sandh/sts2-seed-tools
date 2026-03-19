from typing import List

from act import Act


class Progress:
    def __init__(self):
        self.discovered_acts = set()
        self.discovered_relics = set()
        self.discovered_epochs = set()
        self.discovered_potions = set()
        self.discovered_cards = set()
        self.discovered_events = set()
        self.completed_ftues = set()
        self.seen_encounters = set()

    def discover_act(self, act: Act):
        self.discovered_acts.add(act)

    def discover_relic(self, relic):
        self.discovered_relics.add(relic)

    def discover_epoch(self, epoch):
        self.discovered_epochs.add(epoch)

    def discover_potion(self, potion):
        self.discovered_potions.add(potion)

    def discover_card(self, card):
        self.discovered_cards.add(card)

    def discover_event(self, event):
        self.discovered_events.add(event)

    def complete_ftue(self, ftue):
        self.completed_ftues.add(ftue)

    def add_seen_encounter(self, encounter):
        self.seen_encounters.add(encounter)

    def is_act_discovered(self, act: Act) -> bool:
        return act in self.discovered_acts
    
    def is_epoch_discovered(self, epoch: str) -> bool:
        return epoch in self.discovered_epochs
    
    def get_locked_relics(self) -> List[str]:
        locked_relics = set()

        # Shared relics
        if not self.is_epoch_discovered("RELIC1_EPOCH"):
            locked_relics.add("UnsettlingLamp")
            locked_relics.add("IntimidatingHelmet")
            locked_relics.add("ReptileTrinket")

        if not self.is_epoch_discovered("RELIC2_EPOCH"):
            locked_relics.add("BookOfFiveRings")
            locked_relics.add("IceCream")
            locked_relics.add("Kusarigama")

        if not self.is_epoch_discovered("RELIC3_EPOCH"):
            locked_relics.add("VexingPuzzlebox")
            locked_relics.add("RippleBasin")
            locked_relics.add("FestivePopper")

        if not self.is_epoch_discovered("RELIC4_EPOCH"):
            locked_relics.add("MiniatureCannon")
            locked_relics.add("TungstenRod")
            locked_relics.add("WhiteStar")

        if not self.is_epoch_discovered("RELIC5_EPOCH"):
            locked_relics.add("TinyMailbox")
            locked_relics.add("JossPaper")
            locked_relics.add("BeatingRemnant")

        # Ironclad relics
        if not self.is_epoch_discovered("IRONCLAD3_EPOCH"):
            locked_relics.add("RedSkull")
            locked_relics.add("PaperPhrog")
            locked_relics.add("RuinedHelmet")

        if not self.is_epoch_discovered("IRONCLAD6_EPOCH"):
            locked_relics.add("SelfFormingClay")
            locked_relics.add("CharonsAshes")
            locked_relics.add("DemonTongue")

        # Silent relics
        if not self.is_epoch_discovered("SILENT3_EPOCH"):
            locked_relics.add("ToughBandages")
            locked_relics.add("PaperKrane")
            locked_relics.add("Tingsha")

        if not self.is_epoch_discovered("SILENT6_EPOCH"):
            locked_relics.add("TwistedFunnel")
            locked_relics.add("SneckoSkull")
            locked_relics.add("HelicalDart")

        # Regent relics
        if not self.is_epoch_discovered("REGENT3_EPOCH"):
            locked_relics.add("FencingManual")
            locked_relics.add("GalacticDust")
            locked_relics.add("LunarPastry")
            
        if not self.is_epoch_discovered("REGENT6_EPOCH"):
            locked_relics.add("Regalite")
            locked_relics.add("MiniRegent")
            locked_relics.add("OrangeDough")

        # Necrobinder relics
        if not self.is_epoch_discovered("NECROBINDER3_EPOCH"):
            locked_relics.add("BoneFlute")
            locked_relics.add("FuneraryMask")
            locked_relics.add("BookRepairKnife")
            
        if not self.is_epoch_discovered("NECROBINDER6_EPOCH"):
            locked_relics.add("IvoryTile")
            locked_relics.add("BigHat")
            locked_relics.add("Bookmark")

        # Defect relics
        if not self.is_epoch_discovered("DEFECT3_EPOCH"):
            locked_relics.add("DataDisk")
            locked_relics.add("SymbioticVirus")
            locked_relics.add("Metronome")
            
        if not self.is_epoch_discovered("DEFECT6_EPOCH"):
            locked_relics.add("GoldPlatedCables")
            locked_relics.add("EmotionChip")
            locked_relics.add("PowerCell")

        return locked_relics