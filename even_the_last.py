# You are given an array of integers.
# You should find the sum of the elements with even indexes
# then multiply this summed number and the final element
from functools import reduce


def checkio(ns):
    return reduce((lambda x, y: x + y), ns[::2]) * ns[-1] if ns else 0

print(checkio([0, 1, 2, 3, 4, 5]) == 30)
print(checkio([1, 3, 5]) == 30)
print(checkio([6]) == 36)
print(checkio([]) == 0)
