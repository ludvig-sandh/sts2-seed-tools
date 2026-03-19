from rng import Rng
from util import get_deterministic_hash_code

## Act
def get_default_list():
    return ["Overgrowth", "Hive", "Glory"]

def get_random_list(seed: str):
    acts = get_default_list()
    rng = Rng(get_deterministic_hash_code(seed))
    if rng.next_bool():
        acts[0] = "Underdocks"
    return acts


if __name__ == "__main__":
    seed = input("Input seed: ")
    print("Acts:", get_random_list(seed))