#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
from counting_sort_complex import counting_sort_complex_tuple

def sort(inputList, maxWordLen):
    listToSort = [(-1, e) for e in inputList]
    for i in reversed(range(maxWordLen)):
        tmp = [(ord(listToSort[j][1][i]), listToSort[j][1]) for j in range(len(listToSort))]
        listToSort = counting_sort_complex_tuple(tmp)
    return listToSort

def radix_sort(inputList, fillLeft):
    maxWordLen = max([len(e) for e in inputList])
    if fillLeft:
        inputListFilled = [e.rjust(maxWordLen) for e in inputList]
    else:
        inputListFilled = [e.ljust(maxWordLen) for e in inputList]
    sortedInput = sort(inputListFilled, maxWordLen)
    return [string.strip(e[1]) for e in sortedInput]

def radix_sort_str(inputList):
    return radix_sort(inputList, False)

def radix_sort_int(inputList):
    inputListStr = [str(e) for e in inputList]
    sortedList = radix_sort(inputListStr, True)
    return [int(e) for e in sortedList]


