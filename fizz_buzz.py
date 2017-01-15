# Write a function that will receive a positive integer and return:
# "Fizz Buzz" if the number is divisible by 3 and by 5;
# "Fizz" if the number is divisible by 3;
# "Buzz" if the number is divisible by 5; 
# The number as a string for other cases.

def checkio(n):
    s = ''
    if n % 3 == 0:
        s += 'Fizz'
    if n % 5 == 0:
        s += 'Buzz' if not s else ' Buzz'
    return s if s else str(n)

print(checkio(15) == "Fizz Buzz")
print(checkio(6) == "Fizz")
print(checkio(5) == "Buzz")
print(checkio(7) == "7")
