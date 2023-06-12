#!/usr/bin/python3
def multiple_returns(sentence):
    lenstr = len(sentence)
    if lenstr == 0:
        return 0, None
    else:
        return lenstr, sentence[0]
