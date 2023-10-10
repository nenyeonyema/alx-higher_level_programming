#!/usr/bin/python3
#  a function that returns a tuple with the
# length of a string and its first character.


def multiple_returns(sentence):
    if sentence == "":
        return None
    else:
        lent = len(sentence)
        first_char = sentence[0]
        return (lent, first_char)
