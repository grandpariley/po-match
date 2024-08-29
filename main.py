import json

from pkg.bucket import generate
from pkg.response import parse


def create_buckets():
    with open('posurvey.posurvey.json', 'r') as json_file:
        data = json.load(json_file)
        responses = [parse(d) for d in data]

        buckets = {
            "risk_tolerance": generate(lambda r: r['risk_tolerance'], responses),
            "environment": generate(lambda r: r['environment'], responses),
            "social": generate(lambda r: r['social'], responses),
            "governance": generate(lambda r: r['governance'], responses)
        }
        with open('response.json', 'w') as response_file:
            json.dump(responses, response_file)
        with open('buckets.json', 'w') as bucket_file:
            json.dump(buckets, bucket_file)


def main():
    create_buckets()


if __name__ == '__main__':
    main()
