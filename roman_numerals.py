# Return a roman numeral given integer value ranging from 1 to 3999

def checkio(n):
    s = ''
    special = {
        4: 'IV', 9: 'IX', 40: 'XL',
        90: 'XC', 400: 'CD', 900: 'CM'
    }
    regular = {
        1: 'I', 5: 'V', 10: 'X',
        50: 'L', 100: 'C',
        500: 'D', 1000: 'M'
    }
    max_tenth = 10 ** (len(str(n)) - 1)
    while n > 0:
        digit = n // max_tenth
        if 5 <= digit < 9:
            rem = (digit * max_tenth) % (5 * max_tenth)
            s += regular[5 * max_tenth] + checkio(rem)
        elif digit == 4 or digit == 9:
            s += special[digit * max_tenth]
        else:
            s += regular[max_tenth] * digit
        n %= max_tenth
        max_tenth //= 10
    return s

if __name__ == '__main__':
    print(checkio(6) == 'VI')
    print(checkio(76) == 'LXXVI')
    print(checkio(13) == 'XIII')
    print(checkio(44) == 'XLIV')
    print(checkio(3999) == 'MMMCMXCIX')
