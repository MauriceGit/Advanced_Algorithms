#!/usr/bin/python
# -*- coding: utf-8 -*-



def sort(inputList, mappingFactor, bucketCount):
    buckets = [[] for i in range(bucketCount)]
    outputList = [0 for i in inputList]

    for e in inputList:
        buckets[int(e*mappingFactor)].append(e)

    for i in range(bucketCount):
        buckets[i].sort()

    index = 0
    for l in buckets:
        for e in l:
            outputList[index] = e
            index += 1

    return outputList

def bucket_sort(inputList):
    uniqueValues = len(set(inputList))

    return sort(inputList, (uniqueValues-1)/float(max(inputList)), uniqueValues)

