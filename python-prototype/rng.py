from dotnetrandom import DotNetRandom

class Rng:
    def __init__(self, seed: int, counter: int = 0):
        self.seed = seed
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