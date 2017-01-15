# You are given an array with positive numbers and a number N.
# You should find the Nth power of the element in the array with the index N.
# If N is outside of the array, then return -1.
# Don't forget that the first element has the index 0.

def index_power(ns, n):
    try:
        x = ns[n]
    except IndexError:
        return -1
    else:
        return x ** n

print(index_power([1, 2, 3, 4], 2) == 9)
print(index_power([1, 3, 10, 100], 3) == 1000000)
print(index_power([0, 1], 0) == 1)
print(index_power([1, 2], 3) == -1)
