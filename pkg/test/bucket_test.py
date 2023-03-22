import unittest

from pkg.bucket import Bucket
from pkg.consts import Constants
from pkg.respondent import Respondent


def get_responses():
    return [
        Respondent(0, 1, 2, 3),
        Respondent(1, 2, 3, 0),
        Respondent(2, 3, 0, 1),
        Respondent(0, 1, 2, 3),
        Respondent(1, 2, 3, 0),
        Respondent(2, 3, 0, 1),
    ]


class BucketTest(unittest.TestCase):
    def test_generate(self):
        Constants.NUMBER_OF_BUCKETS = 3
        bucket = Bucket(lambda r: r.risk_tolerance, get_responses())
        self.assertEqual(bucket.data, [0, 0, 1, 1, 2, 2])
        self.assertEqual(bucket.buckets, [(None, 1), (1, 2), (2, None)])
        bucket = Bucket(lambda r: r.environment, get_responses())
        self.assertEqual(bucket.data, [1, 1, 2, 2, 3, 3])
        self.assertEqual(bucket.buckets, [(None, 2), (2, 3), (3, None)])
        bucket = Bucket(lambda r: r.social, get_responses())
        self.assertEqual(bucket.data, [0, 0, 2, 2, 3, 3])
        self.assertEqual(bucket.buckets, [(None, 2), (2, 3), (3, None)])
        bucket = Bucket(lambda r: r.governance, get_responses())
        self.assertEqual(bucket.data, [0, 0, 1, 1, 3, 3])
        self.assertEqual(bucket.buckets, [(None, 1), (1, 3), (3, None)])


if __name__ == '__main__':
    unittest.main()
