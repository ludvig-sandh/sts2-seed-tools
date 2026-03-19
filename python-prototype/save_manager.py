import json

from os import path

from progress import Progress, Act

def read_save_file_as_json(path):
    with open(path, 'r') as fp:
        return json.load(fp)
        
class SaveManager:
    DISCOVERED_ACTS_KEY = "discovered_acts"

    def __init__(self):
        self.progress = Progress()

    def parse_discovered_acts(self, progress_json):
        discovered_acts_json = progress_json[self.DISCOVERED_ACTS_KEY]
        for discovered_act_name in discovered_acts_json:
            act = Act.create_from_name(discovered_act_name)
            self.progress.unlock_act(act)

    def parse_progress_json(self, progress_json) -> Progress:
        print(*progress_json.keys(), sep="\n")

        self.parse_discovered_acts(progress_json)
        
        return self.progress

def load_progress_save_file():
    path_to_progress_file = input("Paste path to directory containing progress.save file: ")
    progress_json = read_save_file_as_json(path.join(path_to_progress_file, "progress.save"))
    progress = SaveManager().parse_progress_json(progress_json)
    return progress

if __name__ == "__main__":
    progress = load_progress_save_file()
    print(progress.unlocked_acts)