# write a function that rounds to hte nearnest 10


def round_nearest_ten(x):
    return round(x, -1)


assert round_nearest_ten(43) == 40
assert round_nearest_ten(78) == 80
assert round_nearest_ten(119) == 120
assert round_nearest_ten(1234) == 1230
print('all test passes')
