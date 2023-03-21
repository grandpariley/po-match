import unittest

from pkg.parse import get_numeric_risk, parse_environment_tolerance, parse_social_tolerance, parse_governance_tolerance


def get_short():
    return {
        "q1": 'A'
    }


def get_long():
    return {
        "q2": "test2",
        "q3": [
            2,
            1,
            0
        ],
        "q4a": 15,
        "q4b": 15,
        "q4c": 15,
        "q5": "A",
        "q6": [
            1,
            None,
            None,
            None,
            0,
            None,
            None,
            None,
            3,
            None,
            2,
            None,
            None,
            None,
            None,
            None
        ],
        "q7": [
            1,
            3,
            4,
            None,
            None,
            0,
            None,
            2,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None
        ],
        "q8": [
            3,
            2,
            0,
            1,
            4,
            5,
            6
        ],
        "q9": "dfgsdfgdfg"
    }


class ParseTest(unittest.TestCase):
    def test_get_numeric_risk(self):
        self.assertEqual(get_numeric_risk('A', 4), -2)
        self.assertEqual(get_numeric_risk('A', 5), -2)
        self.assertEqual(get_numeric_risk('B', 4), -1)
        self.assertEqual(get_numeric_risk('B', 5), -1)
        self.assertEqual(get_numeric_risk('C', 4), 1)
        self.assertEqual(get_numeric_risk('C', 5), 0)
        self.assertEqual(get_numeric_risk('D', 4), 2)
        self.assertEqual(get_numeric_risk('D', 5), 1)
        self.assertEqual(get_numeric_risk('E', 5), 2)

    def test_parse_environment_tolerance(self):
        bad_short = get_short()
        bad_short['q1'] = 'B'
        self.assertEqual(parse_environment_tolerance(bad_short, get_long()), 0)
        self.assertEqual(parse_environment_tolerance(get_short(), None), 0)
        self.assertEqual(parse_environment_tolerance(get_short(), get_long()), 1.4)
        bad_long = get_long()
        bad_long['q5'] = 'B'
        self.assertEqual(parse_environment_tolerance(get_short(), bad_long), 1.15)

    def test_parse_social_tolerance(self):
        bad_short = get_short()
        bad_short['q1'] = 'B'
        self.assertEqual(parse_social_tolerance(bad_short, get_long()), 0)
        self.assertEqual(parse_social_tolerance(get_short(), None), 0)
        self.assertEqual(parse_social_tolerance(get_short(), get_long()), 1.4)
        bad_long = get_long()
        bad_long['q5'] = 'B'
        self.assertEqual(parse_social_tolerance(get_short(), bad_long), 1.15)

    def test_parse_governance_tolerance(self):
        bad_short = get_short()
        bad_short['q1'] = 'B'
        self.assertEqual(parse_governance_tolerance(bad_short, get_long()), 0)
        self.assertEqual(parse_governance_tolerance(get_short(), None), 0)
        self.assertEqual(parse_governance_tolerance(get_short(), get_long()), 2.15)
        bad_long = get_long()
        bad_long['q5'] = 'B'
        self.assertEqual(parse_governance_tolerance(get_short(), bad_long), 1.15)


if __name__ == '__main__':
    unittest.main()
