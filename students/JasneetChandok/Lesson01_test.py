from Lesson01 import Square


class squaretest:
    @staticmethod
    def test_postive_number():
        squares = {
            1: 1,
            2: 4,
            3: 9,
            12: 144,
            100: 10000,
        }

        for num, square in squares.items():
            result = Square.calc(num)
            if result != Square:
                print("Squared{} and {} but expected {}".format(num, result, square))
