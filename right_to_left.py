# You are given a sequence of strings.
# You should join these strings into chunk of text where
# the initial strings are separated by commas.
# Replace all cases of the words "right" with the word "left",
# even if it's a part of another word.
# All strings are given in lowercase.
import re

def left_join(seq):
    return re.sub(r'right', 'left', ','.join(seq))

print(left_join(("left", "right", "left", "stop")) == "left,left,left,stop")
print(left_join(("bright aright", "ok")) == "bleft aleft,ok")
print(left_join(("brightness wright",)) == "bleftness wleft")
print(left_join(("enough", "jokes")) == "enough,jokes")
