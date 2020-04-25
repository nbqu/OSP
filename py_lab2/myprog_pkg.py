#!/usr/bin/python3
from .my_pkg.conversion import convert
from .my_pkg.union_intersection import set_op


while True:
    menu = input("Select menu: 1) conversion 2) union/intersection 3) exit ?")
    if menu == 1 :
        convert()
    if menu == 2 :
        set_op()
    if menu == 3 :
        break
