from math import floor

from pkg.consts import Constants


def generate(getter, responses):
    data = sorted([getter(r) for r in responses])
    buckets = []
    i = 0
    step = floor(len(data) / Constants.NUMBER_OF_BUCKETS)
    for _ in range(Constants.NUMBER_OF_BUCKETS):
        if i == 0:
            buckets.append((None, data[i + step]))
        elif i + step >= len(data):
            buckets.append((data[i], None))
        else:
            buckets.append((data[i], data[i + step]))
        i += step
    return buckets


def get(response, all_buckets, bucket_type):
    buckets = all_buckets[bucket_type]
    r = response[bucket_type]
    for b in buckets:
        if b[0] is None and b[1] > r:
            return b
        elif b[1] is None and b[0] <= r:
            return b
        elif b[0] is not None and b[1] is not None and b[0] <= r < b[1]:
            return b
    raise ValueError('No bucket found!')
