__author__ = 'k'

import unittest
import util


class MyTestCase(unittest.TestCase):
    def test_util_generate_random_vector(self):
        v = util.Vector()
        self.assertEqual("XX-XX-XX-XX-XX-XX", v.get_vector())

    def test_util_generate_random_letter(self):
        self.assertEqual("A", util.letter())


if __name__ == '__main__':
    unittest.main()
