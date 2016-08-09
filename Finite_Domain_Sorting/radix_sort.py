#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""
Radix-Sort. Uses a complex version of Countingsort!
The used countingsort is not very thought through... Could have been modelled better.
Please provide a pull request if you have a good idea.
"""
__author__ = "Maurice Tollmien"
__maintainer__ = "Maurice Tollmien"
__email__ = "maurice.tollmien@gmail.com"

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

# Can be used directly, as Radixsort sorts words
def radix_sort_str(inputList):
    return radix_sort(inputList, False)

# Must be converted to 'words' so the basic Radix-sort can be applied.
# But we can now sort numbers.
def radix_sort_int(inputList):
    inputListStr = [str(e) for e in inputList]
    sortedList = radix_sort(inputListStr, True)
    return [int(e) for e in sortedList]


