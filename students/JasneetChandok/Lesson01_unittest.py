import unittest

from Lesson01 import Square


class SquareTest(unittest.TestCase):
    def test_positive_numbers(self):
        squares = {
            1: 1,
            2: 4,
            3: 9,
            12: 144,
            100: 10000,
        }

        for num, square in squares.items():
            self.assertEqual(square, Square.calc(num), "Squaring {}".format(num))
