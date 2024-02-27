import json
from pathlib import Path
from pkg.bucket import generate
from pkg.respondent import parse

BUCKET_FILE = 'buckets.json'
DATA_FILE = 'posurvey.posurvey.json'
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
        with open(RESPONSE_FILE, 'a') as response_file:
            json.dump(responses, response_file)
        with open(BUCKET_FILE, 'a') as bucket_file:
            json.dump(buckets, bucket_file)


def main():
    if not Path(BUCKET_FILE).exists() or not Path(RESPONSE_FILE).exists():
        create_buckets()


if __name__ == '__main__':
    main()
