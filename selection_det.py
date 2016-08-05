#!/usr/bin/python
# -*- coding: utf-8 -*-

import statistics

def partition(pivot, A):
    smaller = []
    equal   = []
    larger  = []
    for p in A:
        if p < pivot:
            smaller.append(p)
        else:
            if p == pivot:
                equal.append(p)
            else:
                larger.append(p)
    return smaller, equal, larger

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def sortSubListsAndMedian(A):
    sortedList = []
    medianList = []
    for smallList in A:
        sortedList.append(sorted(smallList))
        medianList.append(statistics.median_low(smallList))
    return sortedList, medianList

def select(k, A):

    bigList = chunks(A, 5)

    subSorted, medians = sortSubListsAndMedian(bigList)

    medianPivot = statistics.median_low(medians)

    smaller, equal, larger = partition(medianPivot, A)

    if k <= len(smaller):
        return select(k, smaller)

    if k <= (len(smaller) + len(equal)):
        return medianPivot

    return select(k - (len(smaller) + len(equal)), larger)

def select_det(k, A):
    return select(k,A)

