#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""
Testing sorting algorithms for elements in finite universes.
Careful, it prints out the results.
"""
__author__ = "Maurice Tollmien"
__maintainer__ = "Maurice Tollmien"
__email__ = "maurice.tollmien@gmail.com"

from counting_sort import counting_sort
from counting_sort_complex import counting_sort_complex
from bucket_sort import bucket_sort
from radix_sort import radix_sort_int, radix_sort_str
import random

if __name__ == '__main__':
    listSize = 100
    bigList = [random.randint(0, listSize) for i in xrange(listSize)]

    print "Finished creating .."

    # Test all sorting
    print counting_sort(bigList)
    print counting_sort_complex(bigList)
    print bucket_sort(bigList)
    print radix_sort_int(bigList)

    # convert numbers to String so we can use radix-sort directly on words.
    stringList = []
    maxWordSize = 15
    for i in range(listSize):
        word = ""
        for j in range(maxWordSize):
            if random.randint(0,10) <= 4:
                word += chr(random.randint(48,91))
        stringList.append(word)

    print radix_sort_str(stringList)



