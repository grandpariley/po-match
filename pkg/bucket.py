from math import floor

from po.pkg.consts import Constants
from pomatch.pkg.weights import OBJECTIVES


def get_buckets(responses):
    buckets = dict()
    for o in OBJECTIVES:
        buckets[o] = generate(lambda r: r[o], responses)
    return buckets


def generate(getter, responses):
    responses = filter(lambda r: bool(r), [getter(r) for r in responses])
    data = sorted(responses)
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
    buckets[-1] = (buckets[-1][0], None)
    return buckets
