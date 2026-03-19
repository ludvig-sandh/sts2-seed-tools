from save_manager import SaveManager
from run_state import RunState
from act import ActGenerator, Act
from util import preprocess_seed
from run_manager import RunManager
from character import Character

from dataclasses import dataclass
from typing import List

@dataclass
class RunResult:
    acts: List["Act"]

def start_run(seed: str):
    seed = preprocess_seed(seed)
    progress = SaveManager.load_progress_save_file()
    acts = ActGenerator.generate_act_list(seed, progress)
    run_state = RunState.create_for_new_run(seed, progress, Character.IRONCLAD)  # TODO: Don't hardcode ironclad

    RunManager.populate_relics(run_state)
    RunManager.generate_rooms(run_state)
    RunManager.enter_act(run_state, 0)

    return RunResult(acts)
    

if __name__ == "__main__":
    seed = input("Input seed: ") or "A"
    run_result = start_run(seed)
    print("Acts:", run_result.acts)
