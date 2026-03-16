from rng import Rng


def int32(x: int) -> int:
    return ((x + 2**31) % 2**32) - 2**31


def get_deterministic_hash_code(s: str) -> int:
    num = 352654597
    num2 = num

    for i in range(0, len(s), 2):
        num = int32(num * 33 ^ ord(s[i]))
        if i == len(s) - 1:
            break
        num2 = int32(num2 * 33 ^ ord(s[i + 1]))

    return int32(num + int32(num2 * 1566083941))


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