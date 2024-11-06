#!/bin/python

import sys

def lonely_integer(a):
    lonely = 0
    for i in a:
        lonely = lonely ^ i
    return lonely

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)

