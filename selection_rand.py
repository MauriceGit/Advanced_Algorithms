#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""
Search for the k-th element of an unsorted list.
"""
__author__ = "Maurice Tollmien"
__maintainer__ = "Maurice Tollmien"
__email__ = "maurice.tollmien@gmail.com"

import random

# Basically Quicksort partition
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

def select(k, A):
    pivotIndex = random.randint(0, len(A)-1)
    pivot = A[pivotIndex]

    smaller, equal, larger = partition(pivot, A)

    if k > len(smaller) and k <= (len(smaller) + len(equal)):
        return pivot

    if k <= len(smaller):
        return select(k, smaller)

    return select(k - (len(smaller) + len(equal)), larger)

def select_rand(k, A):
    return select(k, A)

