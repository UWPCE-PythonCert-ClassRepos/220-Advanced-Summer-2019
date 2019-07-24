from square.square import Squarer

class SquarerTest:

    @staticmethod
    def test_positive_numbers():
        squares = {
            1: 1,
            2: 4,
            3: 9,
            12: 144,
            100: 10000,
        }

        for num, square in squares.items():
            result = Squarer.calc(num)

            if result != square:
                print(f"Squared {num} and got {result} but expected {square}")


    @staticmethod
    def test_negitive_numbers():
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