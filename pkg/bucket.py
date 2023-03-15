from pkg.consts import Constants


class Bucket:
    def __init__(self, getter, responses):
        self.data = [getter(r) for r in responses]
        self.buckets = []
        self._generate()

    def _generate(self):
        sorted_data = sorted(self.data)
        i = 0
        for _ in range(Constants.NUMBER_OF_BUCKETS):
            self.buckets.append((sorted_data[i], sorted_data[i + (len(sorted_data) / Constants.NUMBER_OF_BUCKETS)]))
            i += (len(sorted_data) / Constants.NUMBER_OF_BUCKETS)
