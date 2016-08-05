#!/usr/bin/python
# -*- coding: utf-8 -*-

from binary_search import binary_search
from interpolation_search import interpolation_search
from quadratic_binary_search import quadratic_binary_search
import random

if __name__ == '__main__':
    listSize = 100000000
    element  = random.randint(0, listSize)
    bigList = [random.randint(0, listSize) for i in xrange(listSize)]
    bigList.sort()

    print "Finished creating and sorting .."
    print "Looking for", element, "in a list of", listSize, "elements."

    binCount  = 0
    intCount  = 0
    quadCount = 0
    testCount = 100

    for i in range(testCount):
        element  = random.randint(0, listSize)
        binOut, c1 = binary_search(bigList, element)
        intOut, c2 = interpolation_search(bigList, element)
        quaOut, c3 = quadratic_binary_search(bigList, element)
        binCount  += c1
        intCount  += c2
        quadCount += c3
        print "binOut: (_, %s), intOut: (_, %s), quaOut: (_, %s)" % (c1, c2, c3)

    print "Over %s tests and %s elements, the average try-count is:\nBinary:\t%s\n Interpolation:\t%s\nQuadratic:\t%s" % \
        (testCount, listSize, binCount/float(testCount), intCount/float(testCount), quadCount/float(testCount))


    # For 10k Elements, it takes:
        # Binary:           12.95
        # Interpolation:    3.48
        # Quadratic:        3.21
    # For 100k Elements, it takes:
        # Binary:           16.13
        # Interpolation:    3.94
        # Quadratic:        3.24
    # For 1m Elements, it takes:
        # Binary:           19.43
        # Interpolation:    4.12
        # Quadratic:        3.6
    # For 10m Elements, it takes:
        # Binary:           22.66
        # Interpolation:    4.49
        # Quadratic:        3.97
    # For 100m Elements, it takes:
        # Binary:           26.02
        # Interpolation:    4.82
        # Quadratic:        4.22
