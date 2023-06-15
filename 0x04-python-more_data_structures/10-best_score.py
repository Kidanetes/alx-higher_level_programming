#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        len1 = len(a_dictionary)
        if len1 == 0:
            return None
        maxx = 0
        for i in a_dictionary:
            if a_dictionary[i] > maxx:
                best_key = i
                maxx = a_dictionary[i]
        return best_key
    return None
