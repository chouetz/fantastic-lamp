import unittest

import alibaba.script as sc


class TestMySum(unittest.TestCase):
    def test_sum_one(self):
        self.assertEqual(1, sc.my_sum(1))

    def test_sum_two(self):
        self.assertEqual(8, sc.my_sum(3, 5))
