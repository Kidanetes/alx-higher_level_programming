#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        num = 0
        len1 = len(roman_string)
        for i in range(len1):
            if roman_string[i] == 'I':
                num = num + 1
            elif roman_string[i] == 'V':
                if roman_string[i - 1] == 'I' and i != 0:
                    num = num + 3
                else:
                    num = num + 5
            elif roman_string[i] == 'X':
                if roman_string[i - 1] == 'I' and i != 0:
                    num = num + 8
                else:
                    num = num + 10
            elif roman_string[i] == 'L':
                if roman_string[i - 1] == 'X' and i != 0:
                    num = num + 30
                else:
                    num = num + 50
            elif roman_string[i] == 'C':
                if roman_string[i - 1] == 'X' and i != 0:
                    num = num + 80
                else:
                    num = num + 100
            elif roman_string[i] == 'D':
                if roman_string[i - 1] == 'C' and i != 0:
                    num = num + 300
                else:
                    num = num + 500
            elif roman_string[i] == 'M':
                if roman_string[i - 1] == 'C' and i != 0:
                    num = num + 800
                else:
                    num = num + 1000
            else:
                return 0
        return num
    return 0
