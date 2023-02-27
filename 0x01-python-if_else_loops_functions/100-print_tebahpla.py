#!/usr/bin/python3
for i in reversed(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
          "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]):
    if ord(i) % 2 != 0:
        i = i.upper()
    print("{}".format(i), end='')
