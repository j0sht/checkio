# You are given a positive integer.
# Your function should calculate the product of the digits excluding any zeroes.
from functools import reduce


def checkio(n):
    return reduce((lambda x,y: x * y), [ int(c) for c in str(n) if c != '0' ])

print(checkio(123405) == 120)
print(checkio(999) == 729)
print(checkio(1000) == 1)
print(checkio(1111) == 1)
