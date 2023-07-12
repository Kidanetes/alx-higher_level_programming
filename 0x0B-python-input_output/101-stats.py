#!/usr/bin/python3
"""a script that reads stdin line by line
and computes metrics"""


if __name__ == "__main__":
    import sys

    size = 0
    dict_x = {}
    status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0
    size = 0

    try:
        for i in sys.stdin:
            i = i.split()
            try:
                if i[-2] in status_codes:
                    if i[-2] in dict_x:
                        dict_x[i[-2]] += 1
                    else:
                        dict_x[i[-2]] = 1
                size = size + int(i[-1])
            except (TypeError, ValueError, IndexError):
                pass
            finally:
                count += 1
                if count == 10:
                    print("File size:", size)
                    for j in sorted(dict_x):
                        print("{}: {}".format(j, dict_x[j]))
                    count = 0
                    size = 0
    except KeyboardInterrupt:
        print("File size:", size)
        for j in sorted(dict_x):
            print("{}: {}".format(j, dict_x[j]))
        raise
