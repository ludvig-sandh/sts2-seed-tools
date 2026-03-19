from dotnetrandom import DotNetRandom
import math
from util import get_deterministic_hash_code

class Rng:
    def __init__(self, seed: int, name: str = None, counter: int = 0):
        self.seed = seed
        if name is not None:
            self.seed = seed + get_deterministic_hash_code(name)

        self.counter = 0
        self.random = DotNetRandom(seed)

        for _ in range(counter):
            self.next_int()

    def next_bool(self):
        self.counter += 1
        return self.random.next(2) == 0

    def next_int(self, max_exclusive=2**31-1):
        self.counter += 1
        return self.random.next(max_exclusive)

    def next_double(self):
        self.counter += 1
        return self.random.next_double()

    def next_float(self, min_val=0.0, max_val=1.0):
        self.counter += 1
        return self.random.next_double() * (max_val - min_val) + min_val
    
    def next_gaussian_int(self, mean: int, std_dev: int, min_val: int, max_val: int) -> int:
        while True:
            d = 1.0 - self.next_double()
            num = 1.0 - self.next_double()
            num2 = math.sqrt(-2.0 * math.log(d)) * math.sin(math.pi * 2.0 * num)
            a = mean + std_dev * num2
            value = round(a)
            if min_val <= value <= max_val:
                return value
            
    @staticmethod
    def unstable_shuffle(lst, rng):
        num = len(lst)
        while num > 1:
            num -= 1
            j = rng.next_int(num + 1)
            lst[j], lst[num] = lst[num], lst[j]
        return lst

    @staticmethod
    def stable_shuffle(lst, rng):
        try:
            baseline = sorted(lst)
        except TypeError:
            baseline = list(lst)

        for i in range(len(lst)):
            lst[i] = baseline[i]

        return Rng.unstable_shuffle(lst, rng)