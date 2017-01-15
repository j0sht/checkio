# You are given an array of numbers (floats).
# You should find the difference between the maximum and minimum element.
# Your function should be able to handle an undefined amount of arguments.
# For an empty argument list, the function should return 0

def checkio(*args):
    return round(max(args) - min(args), 3) if args else 0

print(checkio(1, 2, 3) == 2)
print(checkio(5, -5) == 10)
print(checkio(10.2, -2.2, 0, 1.1, 0.5) == 12.4)
print(checkio() == 0)
