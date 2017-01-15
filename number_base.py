# My solution
def checkio(s, base):
    letters_to_nums = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(10,37)))
    result, pos = 0, 0
    for n in s[::-1]:
        try:
            n = int(n)
        except ValueError:
            n = letters_to_nums[n]
        if n > (base - 1):
            return -1
        result += n * (base ** pos)
        pos += 1
    return result

# Better solution from checkIO
def checkio_better(str_number, radix):
    try:
        return int(str_number, base=radix)
    except ValueError:
        return -1

print(checkio("AF", 16) == 175)
print(checkio("101", 2) == 5)
print(checkio("101", 5) == 26)
print(checkio("Z", 36) == 35)
print(checkio("AB", 10) == -1)
