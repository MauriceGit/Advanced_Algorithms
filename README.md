# Advanced Algorithms

This repository contains some more advanced algorithms for sorting, sorting in finite universes, searching and trees.
For some algorithms there are short or more advanced tests.

Please see the appropriate file for the exact algorithm.

These implementations were done accompanying a masters lecture on algorithmics.
Some of these algorithms are just implemented quick-and-dirty while others (2,3-tree) have gotten some more thought put into.
I couldn't always find time.

None of the algorithms are fit and ready for production use. But most of them are available as robust implementations in standard or other libraries. Educational purpose only.

## Tree

Algorithm | Runtime
--- | ---
[2,3-tree](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/Tree/23Tree.py) (special case of the a,b-tree) | All operations in θ(logn) w.c. and a.c.

## General Sorting

Algorithm | Runtime |
--- | ---
[Mergesort](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/General_Sorting/mergesort.py) | O(n logn)
[Quicksort](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/General_Sorting/quicksort.py) | O(n^2)

## Sorting in finite domains

n = number of values

k = number of different values

s = max word length (Radixsort)

Algorithm | Runtime
--- | ---
[Countingsort](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/Finite_Domain_Sorting/counting_sort.py) | θ(n+k) w.c. and a.c.
[Advanced Countingsort](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/Finite_Domain_Sorting/counting_sort_complex.py) | θ(n+k) w.c. and a.c.
[Bucketsort](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/Finite_Domain_Sorting/bucket_sort.py) | θ(n+k) w.c. and a.c.
[Radixsort](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/Finite_Domain_Sorting/radix_sort.py) | θ(s*(n+k)) w.c. and a.c.

## Order statistics (Select algorithms)

Searching for the n-th element in a not sorted list.

Algorithm | Runtime
--- | ---
[Randomised Algorithm](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/Selection/selection_rand.py) | θ(n^2) w.c. θ(n) a.c.
[Deterministic Algorithm](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/Selection/selection_det.py) | θ(n) w.c. and a.c.

## Searching in sorted Arrays

Algorithm | Runtime
--- | ---
[Binary Search](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/Searching/binary_search.py) | θ(logn)
[Interpolation Search](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/Searching/interpolation_search.py) | θ(n) w.c. θ(log(logn)) a.c.
[Quadratic Binary Search](https://github.com/MauriceGit/Advanced_Algorithms/blob/master/Searching/quadratic_binary_search.py) | θ(sqrt(n)) w.c. θ(log(logn)) a.c.
