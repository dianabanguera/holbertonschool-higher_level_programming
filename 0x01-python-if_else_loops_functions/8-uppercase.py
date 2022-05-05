#!/usr/bin/python3
def uppercase(str):
    for d in str:
        if ord('a') <= ord(d) <= ord('z'):
            k = chr(ord(d) - (ord('a') - ord('A')))
        print("{:s}".format(d), end='')
    print("")
