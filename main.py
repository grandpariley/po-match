import json

from pomatch.pkg.bucket import generate
from pomatch.pkg.response import parse

OBJECTIVES = ['risk_tolerance', 'environment', 'social', 'governance']


def response_to_weight(response, extremes):
    risk_tolerance = (response['risk_tolerance'] - extremes['risk_tolerance']['min']) / (
            extremes['risk_tolerance']['max'] - extremes['risk_tolerance']['min']) / 4
    environment = (response['environment'] - extremes['environment']['min']) / (
            extremes['environment']['max'] - extremes['environment']['min']) / 4
    social = (response['social'] - extremes['social']['min']) / (
            extremes['social']['max'] - extremes['social']['min']) / 4
    governance = (response['governance'] - extremes['governance']['min']) / (
            extremes['governance']['max'] - extremes['governance']['min']) / 4
    ret = 1 - (risk_tolerance + environment + social + governance)
    return {
        "portfolio_id": response['portfolio_id'],
        "var": risk_tolerance / 2,
        "cvar": risk_tolerance / 2,
        "return": ret,
        "environment": environment,
        "social": social,
        "governance": governance
    }


def get_responses(raw):
    return list(filter(lambda d: all(v is not None for v in d.values()), [parse(d) for d in raw]))


def get_weights(responses):
    extremes = dict()
    for o in OBJECTIVES:
        extremes[o] = {
            'max': None,
            'min': None
        }
        extremes[o]['max'] = max([response[o] for response in responses])
        extremes[o]['min'] = min([response[o] for response in responses])
    weights = [response_to_weight(response, extremes) for response in responses]
    return weights


def get_buckets(responses):
    buckets = dict()
    for o in OBJECTIVES:
        buckets[o] = generate(lambda r: r[o], responses)
    return buckets


def main():
    responses = get_responses()
    buckets = get_buckets(responses)
    weights = get_weights(responses)
    with open('response.json', 'w') as response_file:
        json.dump(responses, response_file)
    with open('weights.json', 'w') as weights_file:
        json.dump(weights, weights_file)
    with open('buckets.json', 'w') as bucket_file:
        json.dump(buckets, bucket_file)


if __name__ == '__main__':
    main()
