from save_manager import SaveManager
from run_state import RunState
from act import ActHelper
from util import preprocess_seed
from run_manager import RunManager
from character import Character
from progress import Progress


def start_run(seed: str, progress: Progress):
    seed = preprocess_seed(seed)
    acts = ActHelper.generate_act_list(seed, progress)
    run_state = RunState.create_for_new_run(seed, progress, acts, Character.IRONCLAD)  # TODO: Don't hardcode ironclad

    RunManager.populate_relics(run_state)
    RunManager.generate_rooms(run_state)
    RunManager.enter_act(run_state, 0)

    return run_state
    

if __name__ == "__main__":
    seed = input("Input seed: ") or "A"
    progress = SaveManager.load_progress_save_file()
    run_state = start_run(seed, progress)
    print("Acts:", run_state.acts)
    print("Player relic bag:", run_state.player_relic_grab_bag)
    print("Act 1 boss: ", run_state.boss_per_act[run_state.acts[0]])
    print("Act 1 normal encounters: ", run_state.normal_encounters_per_act[run_state.acts[0]])
    print("Act 1 elite encounters: ", run_state.elite_encounters_per_act[run_state.acts[0]])
