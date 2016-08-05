#!/usr/bin/python
# -*- coding: utf-8 -*-

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

