# Advanced Algorithms

This repository contains some more advanced algorithms for sorting, sorting in finite universes, searching and trees.
For some algorithms there are short or more advanced tests.

Please see the appropriate file for the exact algorithm.

## Tree

| Algorithm | Runtime |
| ---------------------------------------- | --- |
| [2,3-tree](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/23Tree.py) (special case of the a,b-tree) | All operations in θ(logn) |

## General Sorting

| Algorithm | Runtime |
| ---------------------------------------- | --- |
| [Mergesort](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/mergesort.py) | O(n logn) |
| [Quicksort](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/quicksort.py) | O(n^2) |

## Sorting in finite domains

n = number of values

k = number of different values

s = max word length (Radixsort)

| Algorithm | Runtime |
| ---------------------------------------- | --- |
| [Countingsort](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/counting_sort.py) | θ(n+k), O(n)
| [Advanced Countingsort](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/counting_sort_complex.py) | θ(n+k), O(n)
| [Bucketsort](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/bucket_sort.py) | θ(n+k), O(n)
| [Radixsort](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/radix_sort.py) | θ(s*(n+k))

## Order statistics (Select algorithms)

Searching for the n-th element in a not sorted list.

| Algorithm | Runtime |
| --- | --- |
| [Randomised Algorithm](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/selection_rand.py) | θ(n^2) w.c. θ(n) a.c.
| [Deterministic Algorithm](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/selection_det.py) | θ(n) w.c. and a.c.

## Searching in sorted Arrays

| Algorithm | Runtime |
| --- | --- |
| [Binary Search](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/binary_search.py) | θ(logn)
| [Interpolation Search](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/interpolation_search.py) | θ(n) w.c. θ(log(logn)) a.c.
| [Quadratic Binary Search](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/quadratic_binary_search.py) | θ(sqrt(n)) w.c. θ(log(logn)) a.c.
