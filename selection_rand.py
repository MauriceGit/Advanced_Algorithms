#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

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

