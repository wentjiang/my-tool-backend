import unittest
from datetime import datetime as dt
import datetime

import application


class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        start_time = dt(2023, 1, 1, 12, 0, 0)
        end_time = dt(2023, 1, 1, 13, 30, 0)
        result = application.calculate_time_diff(start_time, end_time)
        self.assertEqual(result, datetime.timedelta(seconds=5400))
