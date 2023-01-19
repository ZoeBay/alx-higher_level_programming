#!/usr/bin/python3
for num in range(0, 9):
    for nm in range(num + 1, 10):
        if num < 8:
            print("{}""{}".format(num, nm), end=', ')
        if num == 8:
            print("{}""{}".format(num, nm), end='\n')
            break
