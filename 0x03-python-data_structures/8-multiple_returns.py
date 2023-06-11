#!/usr/bin/python3
""" returns a tuple with the length of a string and its first character. """


def multiple_returns(sentence):
    if sentence is not None:
        return (len(sentence), sentence[:1]) if len(sentence) != 0 else (len(sentence), None)
sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))