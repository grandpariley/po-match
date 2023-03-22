from math import floor

from pkg.consts import Constants


class Bucket:
    def __init__(self, getter, responses):
        self.data = sorted([getter(r) for r in responses])
        self.buckets = []
        self._generate()

    def _generate(self):
        i = 0
        step = floor(len(self.data) / Constants.NUMBER_OF_BUCKETS)
        for _ in range(Constants.NUMBER_OF_BUCKETS):
            if i == 0:
                self.buckets.append((None, self.data[i + step]))
            elif i + step >= len(self.data):
                self.buckets.append((self.data[i], None))
            else:
                self.buckets.append((self.data[i], self.data[i + step]))
            i += step
