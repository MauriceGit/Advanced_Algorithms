#!/usr/bin/python
import random
import time

def merge (l1, l2):
	i = 0
	j = 0
	newList = []
	while i < len(l1) and j < len(l2):
		if l1[i] < l2[j]:
			newList.append(l1[i])
			i = i+1
		else:
			newList.append(l2[j])
			j = j+1
	while i < len(l1):
		newList.append(l1[i])
		i = i+1
	while j < len(l2):
		newList.append(l2[j])
		j = j+1
	return newList			

def mergeSort (l):
	
	if len(l) <= 1:
		return l	
	
	firstHalf  = mergeSort (l[:len(l)/2])
	secondHalf = mergeSort (l[len(l)/2:])
	
	return merge(firstHalf, secondHalf)
	
size = 1000000
unsortedList = range(size)
#random.shuffle(unsortedList)

#unsortedList.reverse()

t0 = time.time()

res =  mergeSort (unsortedList)

print time.time() - t0

#print res
