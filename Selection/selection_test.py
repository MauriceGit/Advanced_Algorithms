#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Testing two selection algorithms (random and deterministic).
Find a random index.
"""
__author__ = "Maurice Tollmien"
__maintainer__ = "Maurice Tollmien"
__email__ = "maurice.tollmien@gmail.com"


from selection_det import select_det
from selection_rand import select_rand
import random
import time

if __name__ == '__main__':
    start = time.clock()
    listSize = 1000000
    index    = random.randint(0, listSize/2)
    bigList = [random.randint(0, listSize) for i in range(listSize)]

    print("{} time: {}".format(index, time.clock()-start))
    start = time.clock()
    print("Selection rand: {}, time: {}".format(select_rand(index, bigList), time.clock()-start))
    start = time.clock()
    print("Selection det: {}, time: {}".format(select_det(index, bigList), time.clock()-start))

