import unittest

from po.pkg.bucket import generate, get
from po.pkg.consts import Constants


def get_responses():
    return [
        {
            "risk_tolerance": 0,
            "environment": 1,
            "social": 2,
            "governance": 3
        },
        {
            "risk_tolerance": 1,
            "environment": 2,
            "social": 3,
            "governance": 0
        },
        {
            "risk_tolerance": 2,
            "environment": 3,
            "social": 0,
            "governance": 1
        },
        {
            "risk_tolerance": 0,
            "environment": 1,
            "social": 2,
            "governance": 3
        },
        {
            "risk_tolerance": 1,
            "environment": 2,
            "social": 3,
            "governance": 0
        },
        {
            "risk_tolerance": 2,
            "environment": 3,
            "social": 0,
            "governance": 1
        },
    ]


def get_buckets():
    return {
        "risk_tolerance": [[None, 1], [1, 2], [2, None]],
        "environment": [[None, 2], [2, 3], [3, None]],
        "social": [[None, 2], [2, 3], [3, None]],
        "governance": [[None, 1], [1, 3], [3, None]]
    }


class BucketTest(unittest.TestCase):
    def test_generate(self):
        Constants.NUMBER_OF_BUCKETS = 3
        bucket = generate(lambda r: r['risk_tolerance'], get_responses())
        self.assertEqual(bucket, [(None, 1), (1, 2), (2, None)])
        bucket = generate(lambda r: r['environment'], get_responses())
        self.assertEqual(bucket, [(None, 2), (2, 3), (3, None)])
        bucket = generate(lambda r: r['social'], get_responses())
        self.assertEqual(bucket, [(None, 2), (2, 3), (3, None)])
        bucket = generate(lambda r: r['governance'], get_responses())
        self.assertEqual(bucket, [(None, 1), (1, 3), (3, None)])

    def test_get(self):
        self.assertEqual(get(get_responses()[0], get_buckets(), "risk_tolerance"), [None, 1])
        self.assertEqual(get(get_responses()[0], get_buckets(), "environment"), [None, 2])
        self.assertEqual(get(get_responses()[0], get_buckets(), "social"), [2, 3])
        self.assertEqual(get(get_responses()[0], get_buckets(), "governance"), [3, None])


if __name__ == '__main__':
    unittest.main()
