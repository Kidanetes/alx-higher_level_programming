#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    names = dir()
    for i in range(i, len(names)):
        if names[i][1] != '_':
            print(names[i])
