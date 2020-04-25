#!/usr/bin/python3
import my_pkg


while True:
    menu = int(input("Select menu: 1) conversion 2) union/intersection 3) exit ?"))
    if menu == 1 :
        my_pkg.convert()
    if menu == 2 :
        my_pkg.set_op()
    if menu == 3 :
        break
