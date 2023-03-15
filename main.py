import json

from pkg.bucket import Bucket
from pkg.respondent import Respondent


def main():
    with open('data.json') as json_file:
        data = json.load(json_file)
        responses = [Respondent(d) for d in data]
        buckets = {
            "risk_tolerance": Bucket(lambda r: r.risk_tolerance, responses).buckets,
            "environment": Bucket(lambda r: r.environment, responses).buckets,
            "social": Bucket(lambda r: r.social, responses).buckets,
            "governance": Bucket(lambda r: r.governance, responses).buckets
        }
        with open('output.json') as output:
            json.dump(buckets, output)


if __name__ == '__main__':
    main()
