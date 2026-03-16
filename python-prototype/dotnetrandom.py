# The RNG used in .NET's Random module
class DotNetRandom:
    MBIG = 2147483647
    MSEED = 161803398
    MZ = 0

    def __init__(self, seed: int):
        self.seed_array = [0] * 56
        self.inext = 0
        self.inextp = 21

        subtraction = abs(seed)
        mj = self.MSEED - subtraction
        mj %= self.MBIG
        self.seed_array[55] = mj
        mk = 1

        for i in range(1, 55):
            ii = (21 * i) % 55
            self.seed_array[ii] = mk
            mk = mj - mk
            if mk < 0:
                mk += self.MBIG
            mj = self.seed_array[ii]

        for _ in range(4):
            for i in range(1, 56):
                self.seed_array[i] -= self.seed_array[1 + (i + 30) % 55]
                if self.seed_array[i] < 0:
                    self.seed_array[i] += self.MBIG

    def internal_sample(self):
        self.inext += 1
        if self.inext >= 56:
            self.inext = 1

        self.inextp += 1
        if self.inextp >= 56:
            self.inextp = 1

        ret = self.seed_array[self.inext] - self.seed_array[self.inextp]

        if ret < 0:
            ret += self.MBIG

        self.seed_array[self.inext] = ret
        return ret

    def next(self, max_value=None):
        if max_value is None:
            return self.internal_sample()

        return int(self.sample() * max_value)

    def sample(self):
        return self.internal_sample() * (1.0 / self.MBIG)

    def next_double(self):
        return self.sample()