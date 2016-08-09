#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""
Search for the index of an element in a sorted list. Basic algorithm.
"""
__author__ = "Maurice Tollmien"
__maintainer__ = "Maurice Tollmien"
__email__ = "maurice.tollmien@gmail.com"

def search(S, e, l, r, count):
    if l > r:
        return -1, count

    index = (r+l)/2

    if e == S[index]:
        return index, count
    if e < S[index]:
        return search(S, e, l, index-1, count+1)
    return search(S, e, index+1, r, count+1)

def binary_search(S, e):
    return search(S, e, 0, len(S)-1, 1)

