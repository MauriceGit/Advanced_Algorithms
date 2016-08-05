#!/usr/bin/python
# -*- coding: utf-8 -*-

def sort(inputList, maxElem):
    outputList = [0 for i in inputList]
    countingList = [0 for i in range(maxElem)]

    for e in inputList:
        countingList[e] += 1

    for i in range(len(countingList)):
        if i > 0:
            countingList[i] += countingList[i-1]

    for i in reversed(range(len(inputList))):
        outputList[countingList[inputList[i]]-1] = inputList[i]
        countingList[inputList[i]] -= 1

    return outputList

# Simple copy&paste. Should be reworked to make it look nicer!
# But more of a quick and dirty version. So not bothering.
def sort_tuple(inputList, maxElem):
    outputList = [0 for i in inputList]
    countingList = [0 for i in range(maxElem)]

    for e in inputList:
        countingList[e[0]] += 1

    for i in range(len(countingList)):
        if i > 0:
            countingList[i] += countingList[i-1]

    for i in reversed(range(len(inputList))):
        outputList[countingList[inputList[i][0]]-1] = inputList[i]
        countingList[inputList[i][0]] -= 1

    return outputList

def counting_sort_complex_tuple(inputList):
    maxElem = max(e[0] for e in inputList)
    return sort_tuple(inputList, maxElem+1)

def counting_sort_complex(inputList):
    return sort(inputList, max(inputList)+1)

