# You are given a chunk of text.
# Gather all capital letters in one word in the order that they appear in the text.

def find_message(s):
    return ''.join([ l for l in s if 'A' <= l <= 'Z'])

print(find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO")
print(find_message("hello world!") == "")
