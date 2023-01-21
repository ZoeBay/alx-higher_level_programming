#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 0 and ord(char) <= 90:
            char = char
        else:
            char = chr(ord(char) - 32)
        print("{}".format(chr(ord(char))), end=' ')
    print('\n')
