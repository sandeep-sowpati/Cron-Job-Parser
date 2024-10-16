from cron.parser import *

import unittest

class TestCronExpressionParser(unittest.TestCase):

    def test_parse_minutes(self):
        self.assertEqual(parse_minutes("*/15"), [0, 15, 30, 45])
        self.assertEqual(parse_minutes("0"), [0])
        self.assertEqual(parse_minutes("1,15,30"), [1, 15, 30])
        self.assertEqual(parse_minutes("1-5"), [1, 2, 3, 4, 5])
        with self.assertRaises(ValueError):
            parse_minutes("60")
    
    def test_parse_hours(self):
        self.assertEqual(parse_hours("*/3"), [0, 3, 6, 9, 12, 15, 18, 21])
        self.assertEqual(parse_hours("0"), [0])
        self.assertEqual(parse_hours("1,12"), [1, 12])
        self.assertEqual(parse_hours("0-5"), [0, 1, 2, 3, 4, 5])
        with self.assertRaises(ValueError):
            parse_hours("24")

    def test_parse_days_of_the_month(self):
        self.assertEqual(parse_days_of_the_month("1,15"), [1, 15])
        self.assertEqual(parse_days_of_the_month("10-20"), list(range(10, 21)))
        self.assertEqual(parse_days_of_the_month("31"), [31])
        self.assertEqual(parse_days_of_the_month("*"), list(range(1, 32)))
        with self.assertRaises(ValueError):
            parse_days_of_the_month("32")

    def test_parse_months(self):
        self.assertEqual(parse_months("*"), list(range(1, 13)))
        self.assertEqual(parse_months("1,6,12"), [1, 6, 12])
        self.assertEqual(parse_months("3-5"), [3, 4, 5])
        with self.assertRaises(ValueError):
            parse_months("13")

    def test_parse_days_of_the_week(self):
        self.assertEqual(parse_days_of_the_week("1-5"), [1, 2, 3, 4, 5])
        self.assertEqual(parse_days_of_the_week("*"), list(range(1, 8)))
        with self.assertRaises(ValueError):
            parse_days_of_the_week("8")
        with self.assertRaises(ValueError):
            parse_days_of_the_week("0,6")

    def test_parse_task(self):
        self.assertEqual(parse_task("/usr/bin/find"), ["/usr/bin/find"])

    def test_parse_full_expression(self):
        expression = "*/15 0 1,15 * 1-5 /usr/bin/find"
        expected_result = {
            'minutes': [0, 15, 30, 45],
            'hours': [0],
            'days_of_the_month': [1, 15],
            'months': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'days_of_the_week': [1, 2, 3, 4, 5],
            'task': ["/usr/bin/find"]
        }
        parsed_data = parse_expression(expression)
        self.assertEqual(parsed_data, expected_result)

if __name__ == '__main__':
    unittest.main()
