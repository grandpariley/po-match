import json
from pathlib import Path
from pkg.bucket import generate, get
from pkg.respondent import parse

BUCKET_FILE = 'buckets.json'
DATA_FILE = 'data.json'
RESPONSE_FILE = 'response.json'


def create_buckets():
    with open(DATA_FILE) as json_file:
        data = json.load(json_file)
        responses = [parse(d) for d in data]
        buckets = {
            "risk_tolerance": generate(lambda r: r['risk_tolerance'], responses),
            "environment": generate(lambda r: r['environment'], responses),
            "social": generate(lambda r: r['social'], responses),
            "governance": generate(lambda r: r['governance'], responses)
        }
        with open(BUCKET_FILE, 'a') as bucket_file:
            json.dump(buckets, bucket_file)


def main():
    if not Path(BUCKET_FILE).exists():
        create_buckets()
    with open(BUCKET_FILE) as bucket_file:
        buckets = json.load(bucket_file)
        with open(RESPONSE_FILE) as response_file:
            response = parse(json.load(response_file))
            print(response)
            print(get(response, buckets, "risk_tolerance"))
            print(get(response, buckets, "environment"))
            print(get(response, buckets, "social"))
            print(get(response, buckets, "governance"))


if __name__ == '__main__':
    main()
