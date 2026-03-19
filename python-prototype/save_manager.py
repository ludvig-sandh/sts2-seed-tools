import json

from os import path

from progress import Progress, Act

def read_save_file_as_json(path):
    with open(path, 'r') as fp:
        return json.load(fp)
        
class SaveManager:
    DISCOVERED_ACTS_KEY = "discovered_acts"
    DISCOVERED_RELICS_KEY = "discovered_relics"
    DISCOVERED_EPOCHS_KEY = "epochs"
    DISCOVERED_POTIONS_KEY = "discovered_potions"
    DISCOVERED_CARDS_KEY = "discovered_cards"
    DISCOVERED_EVENTS_KEY = "discovered_events"
    COMPLETED_FTUES_KEY = "ftue_completed"
    ENCOUNTER_STATS_KEY = "encounter_stats"

    def __init__(self):
        self.progress = Progress()

    def parse_discovered_acts(self, progress_json):
        discovered_acts_json = progress_json[self.DISCOVERED_ACTS_KEY]
        for discovered_act_name in discovered_acts_json:
            act = Act.create_from_name(discovered_act_name)
            self.progress.discover_act(act)

    def parse_discovered_relics(self, progress_json):
        discovered_relics_json = progress_json[self.DISCOVERED_RELICS_KEY]
        for discovered_relic_name in discovered_relics_json:
            self.progress.discover_relic(discovered_relic_name)

    def parse_discovered_epochs(self, progress_json):
        discovered_epochs_json = progress_json[self.DISCOVERED_EPOCHS_KEY]
        for discovered_epoch in discovered_epochs_json:
            if discovered_epoch["state"] == "revealed":
                epoch_id = discovered_epoch["id"]
                self.progress.discover_epoch(epoch_id)

    def parse_discovered_potions(self, progress_json):
        discovered_potions_json = progress_json[self.DISCOVERED_POTIONS_KEY]
        for discovered_potion_name in discovered_potions_json:
            self.progress.discover_potion(discovered_potion_name)

    def parse_discovered_cards(self, progress_json):
        discovered_cards_json = progress_json[self.DISCOVERED_CARDS_KEY]
        for discovered_card_name in discovered_cards_json:
            self.progress.discover_card(discovered_card_name)

    def parse_discovered_events(self, progress_json):
        discovered_events_json = progress_json[self.DISCOVERED_EVENTS_KEY]
        for discovered_event_name in discovered_events_json:
            self.progress.discover_event(discovered_event_name)

    def parse_completed_ftues(self, progress_json):
        completed_ftues = progress_json[self.COMPLETED_FTUES_KEY]
        for completed_ftue_name in completed_ftues:
            self.progress.complete_ftue(completed_ftue_name)

    def parse_encounter_stats(self, progress_json):
        encounters = progress_json[self.ENCOUNTER_STATS_KEY]
        for encounter in encounters:
            self.progress.add_seen_encounter(encounter["encounter_id"])

    def parse_progress_json(self, progress_json) -> Progress:
        self.parse_discovered_acts(progress_json)
        self.parse_discovered_relics(progress_json)
        self.parse_discovered_epochs(progress_json)
        self.parse_discovered_potions(progress_json)
        self.parse_discovered_cards(progress_json)
        self.parse_discovered_events(progress_json)
        self.parse_completed_ftues(progress_json)
        self.parse_encounter_stats(progress_json)
        return self.progress

    @staticmethod
    def load_progress_save_file():
        path_to_progress_file = input("Paste path to directory containing progress.save file: ")
        progress_json = read_save_file_as_json(path.join(path_to_progress_file, "progress.save"))
        progress = SaveManager().parse_progress_json(progress_json)
        return progress

if __name__ == "__main__":
    progress = SaveManager.load_progress_save_file()
    print(progress.seen_encounters)