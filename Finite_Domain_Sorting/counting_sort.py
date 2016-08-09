#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""
Sorting of elements with a finite amount k of different values!! This is very important. Runs in Theta(n+k).
"""
__author__ = "Maurice Tollmien"
__maintainer__ = "Maurice Tollmien"
__email__ = "maurice.tollmien@gmail.com"

def sort(inputList, maxElem):
    outputList = [0 for i in inputList]
    countingList = [0 for i in range(maxElem)]

    for e in inputList:
        countingList[e] += 1

    index = 0
    for e in range(len(countingList)):
        for i in range(countingList[e]):
            outputList[index] = e
            index += 1
    return outputList

def counting_sort(inputList):
    return sort(inputList, max(inputList)+1)

