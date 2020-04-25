#!/usr/bin/python3
def convert():
    num = int(input("input binary number : "), base=2)
    print("=> OCT> %s" % oct(num)[2:])
    print("=> DEC> %d" % num)
    print("=> HEX> %s" % hex(num)[2:].upper())
