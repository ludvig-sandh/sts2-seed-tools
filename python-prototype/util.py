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

def preprocess_seed(seed: str) -> str:
    seed = seed.upper()
    seed = seed.replace('O', '0')
    seed = seed.replace('I', '1')
    seed = seed.strip()
    return seed