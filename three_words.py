# You are given a string with words and numbers separated by whitespaces.
# The words contains only letters.
# You should check if the string contains three words in succession.
import re


def checkio(s):
    return re.search(r'[a-zA-Z]+\s[a-zA-Z]+\s[a-zA-Z]+', s) != None

print(checkio("Hello World hello") == True)
print(checkio("He is 123 man") == False)
print(checkio("1 2 3 4") == False)
print(checkio("bla bla bla bla") == True)
print(checkio("Hi") == False)
