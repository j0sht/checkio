# You are given a non-empty list of integers (X).
# For this task, you should return a list consisting of only
# the non-unique elements in this list.
# You will need to remove all unique elements
# When solving this task, do not change the order of the list.
# Example: [1, 2, 3, 1, 3] => [1, 3, 1, 3]


# def checkio(xs):
#    frequency = {}
#    for x in xs:
#        frequency[x] = frequency.setdefault(x, 0) + 1
#    return list(filter((lambda x: frequency[x] > 1), xs))

def checkio(data):
    return [ n for n in data if data.count(n) > 1 ]

print(checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3])
print(checkio([1, 2, 3, 4, 5]) == [])
print(checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5])
print(checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9])
