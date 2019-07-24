import unittest
from square.square import Squarer

class SquarerTest(unittest.TestCase):

    def test_positive_numbers(self):
        squares = {
            1: 1,
            2: 4,
            3: 9,
            12: 144,
            100: 10000,
        }

        for num, square in squares.items():
            self.assertEqual(square, Squarer.calc(num), "Squaring {}".format(num))


    def test_negitive_numbers(self):
        squares = {
            -1: 1,
            -2: 4,
            -3: 9,
            -12: 144,
            -100: 10000,
        }

        for num, square in squares.items():
            result = Squarer.calc(num)

            if result != square:
               print(f"Squared {num} and got {result} but expected {square}")


# Example test
class Demo(unittest.TestCase):
    productCode = "AAAA7777"
    inventory = Inventory(productCode)
    def compare_dict(self):
        self.assertDictEqual({}, {}, inventory.returnAsDictionary())