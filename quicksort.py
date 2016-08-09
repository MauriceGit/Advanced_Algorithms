#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""
Quicksort... You know, right? :)
"""
__author__ = "Maurice Tollmien"
__maintainer__ = "Maurice Tollmien"
__email__ = "maurice.tollmien@gmail.com"

from random import randint
import random
import time

def split(leftI, rightI):
    pivot = rightI
    i = leftI
    j = rightI
    while i < j:
        while l[i] <= l[pivot] and i < rightI:
            i = i+1
        while l[j] >= l[pivot] and j >= leftI:
            j = j-1
        if i < j:
            tmp = l[j]
            l[j] = l[i]
            l[i] = tmp
    if l[i] > l[pivot]:
        tmp = l[pivot]
        l[pivot] = l[i]
        l[i] = tmp
    return i

def quickSort (leftI, rightI):
    if leftI < rightI:
        splitter = split(leftI, rightI)
        quickSort(leftI, splitter-1)
        quickSort(splitter+1, rightI)


# Some small tests
if __name__ == '__main__':
    size = 1000000
    l = range(size)
    #random.shuffle(l)

    #l.reverse()

    t0 = time.time()

    quickSort (0, size-1)

    print time.time() - t0

    #print l
