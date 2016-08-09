#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""
Find the index of an element in a sorted List.
"""
__author__ = "Maurice Tollmien"
__maintainer__ = "Maurice Tollmien"
__email__ = "maurice.tollmien@gmail.com"

import math

def findLeftInterval(S, e, stepSize, start):
    thisStep = start-stepSize
    while e < S[thisStep] and thisStep > 0:
        thisStep -= stepSize

    return max(0, thisStep)

def findRightInterval(S, e, stepSize, start):
    length = len(S)
    thisStep = start+stepSize
    while thisStep < length and e > S[thisStep]:
        thisStep += stepSize

    return min(thisStep, length-1)

def search(S, e, l, r, count):
    # second check to avoid possible division by zero later on
    if l > r or S[l] == S[r]:
        return -1, count

    percentage = float(e-S[l]) / float(S[r]-S[l])

    # When the element we are looking for is outside the given range
    if percentage > 1.0 or percentage < 0.0:
        return -1, count

    index = int(round(percentage * (r-l) + l))

    if e == S[index]:
        return index, count
    if e < S[index]:
        return search(S, e, findLeftInterval(S, e, int(math.sqrt(index-1-l)), index-1), index-1, count+1)
    return search(S, e, index+1, findRightInterval(S, e, int(math.sqrt(r-(index+1))), index+1), count+1)

def quadratic_binary_search(S, e):
    return search(S, e, 0, len(S)-1, 1)

