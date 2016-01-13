__author__ = 'k'

import unittest
import util


class MyTestCase(unittest.TestCase):
    def test_util_generate_vector(self):
        self.assertEqual("XX-XX-XX-XX-XX-XX", util.generate_vector())

    def test_util_generate_random_vector(self):
        self.assertEqual("XX-XX-XX-XX-XX-XX", util.generate_random_vector())

    def test_util_generate_random_letter(self):
        self.assertEqual("A", util.random_letter())


if __name__ == '__main__':
    unittest.main()
