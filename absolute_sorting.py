def checkio(ns):
    return sorted(ns, key=abs)

print(checkio((-20, -5, 10, 15)) == [-5, 10, 15, -20])
print(checkio((1, 2, 3, 0)) == [0, 1, 2, 3])
print(checkio((-1, -2, -3, 0)) == [0, -1, -2, -3])
