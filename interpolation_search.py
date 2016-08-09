#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""
Search for the index of an element in a sorted list.
"""
__author__ = "Maurice Tollmien"
__maintainer__ = "Maurice Tollmien"
__email__ = "maurice.tollmien@gmail.com"

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
        return search(S, e, l, index-1, count+1)
    return search(S, e, index+1, r, count+1)

def interpolation_search(S, e):
    return search(S, e, 0, len(S)-1, 1)

