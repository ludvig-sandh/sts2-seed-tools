from save_manager import SaveManager
from run_state import RunState
from act import ActGenerator, Act
from util import preprocess_seed

from dataclasses import dataclass
from typing import List

@dataclass
class RunResult:
    acts: List["Act"]

def start_run(seed: str):
    seed = preprocess_seed(seed)
    progress = SaveManager.load_progress_save_file()
    acts = ActGenerator.generate_act_list(seed, progress)
    run_state = RunState.create_for_new_run(seed)
    return RunResult(acts)
    

if __name__ == "__main__":
    seed = input("Input seed: ") or "A"
    run_result = start_run(seed)
    print("Acts:", run_result.acts)
