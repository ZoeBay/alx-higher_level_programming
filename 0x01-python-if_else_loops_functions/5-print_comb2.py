#/usr/bin/python3
for num in range(0, 10):
    for nm in range(0, 10):
        if nm < 9:
            print("{}""{}".format(num, nm), end=', ')
        if nm == 9:
            print("{}""{}".format(num, nm), end='\n')
            break
