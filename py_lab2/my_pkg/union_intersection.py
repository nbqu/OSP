#!/usr/bin/python3
import re


def set_op():
    a = input()
    b = input()
    a_set = set()
    b_set = set()

    for i in re.split('\W+', a):
        if i != '':
            a_set.add(int(i))
    for i in re.split('\W+', b):
        if i != '':
            b_set.add(int(i))

    print("union ", list(set.union(a_set, b_set)))
    print("intersection ", list(set.intersection(a_set, b_set)))

