#!/usr/bin/python
# -*- coding: utf-8 -*-

from counting_sort import counting_sort
from counting_sort_complex import counting_sort_complex
from bucket_sort import bucket_sort
from radix_sort import radix_sort_int, radix_sort_str
import random

if __name__ == '__main__':
    listSize = 100
    bigList = [random.randint(0, listSize) for i in xrange(listSize)]

    print "Finished creating .."

    print counting_sort(bigList)
    print counting_sort_complex(bigList)
    print bucket_sort(bigList)
    print radix_sort_int(bigList)

    stringList = []
    maxWordSize = 15
    for i in range(listSize):
        word = ""
        for j in range(maxWordSize):
            if random.randint(0,10) <= 4:
                word += chr(random.randint(48,91))
        stringList.append(word)

    print radix_sort_str(stringList)



