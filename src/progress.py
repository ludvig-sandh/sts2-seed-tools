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