#!/bin/python

import sys
import os

def countX(steps):
    minR = 9999999L
    minC = 9999999L
    for step in steps:
        (rStr, cStr) = step.split()
        r = int(rStr)
        c = int(cStr)
        if r < minR:
            minR = r
        if c < minC:
            minC = c
    if minR > minC:
        return long(minR)
    else:
        return long(minC)


if __name__ == "__main__":
    f = open('./bbb', 'w')
    steps_cnt = 0
    steps_cnt = int(raw_input())
    steps_i = 0
    steps = []
    while steps_i < steps_cnt:
        try:
            steps_item = raw_input()
        except:
            steps_item = None
        steps.append(steps_item)
        steps_i += 1


    res = countX(steps);
    f.write(str(res) + "\n")

    f.close()
