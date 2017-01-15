# Return a roman numeral given integer value ranging from 1 to 3999

def checkio(n):
    s = ''
    romans = {
        1: 'I', 4: 'IV', 5: 'V',
        9: 'IX', 10: 'X', 40: 'XL',
        50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }
    while n > 0:
        max_tenth = 10 ** (len(str(n)) - 1)
        digit = n // max_tenth
        if 5 <= digit < 9:
            rem = (digit % 5) * max_tenth
            s += romans[5 * max_tenth] + checkio(rem)
        elif digit == 4 or digit == 9:
            s += romans[digit * max_tenth]
        else:
            s += romans[max_tenth] * digit
        n %= max_tenth
    return s

if __name__ == '__main__':
    print(checkio(6) == 'VI')
    print(checkio(76) == 'LXXVI')
    print(checkio(13) == 'XIII')
    print(checkio(44) == 'XLIV')
    print(checkio(3999) == 'MMMCMXCIX')
