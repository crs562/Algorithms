# Algorithms

## Problem 1 : Sum of Two Digits
**Task** : Compute the sum of two single digit numbers. <br/>
**Input** : Two single digit numbers. <br/>
**Output** : The sum of these numbers. <br/>

## Problem 2 : Maximum Pairwise Product
**Task** : Find the maximum product of two distinct numbers in a sequence of non-negative integers. <br/>
**Input** : An integer 2 <= n <= 2x10^5 and a sequence of n non-negative integers. <br/>
**Output** : The maximum value that can be obtained by multiplying two different elements from the sequence. <br/>

## Problem 3 : Fibonacci Number
**Task** : Compute the n-th Fibonacci number. <br/>
**Input** : An integer 0 <= n <= 45. <br/>
**Output** : n-th Fibonacci number.

## Problem 4 : Last Digit of Fibonnacci Number
**Task** : Compute the last digit of the n-th Fibonacci number. <br/>
**Input** : An integer 0 <= n <= 10^6. <br/>
**Output** : The last digit of the n-th Fibonacci number.

## Problem 5 : Greatest Common Divisor
**Task** : Compute the greatest common divisor of two positive integers. <br/>
**Input** : Two positive integers 1 <= a, b <= 2x10^9. <br/>
**Output** : The greatest common divisor of a and b.

## Problem 6 : Least Common Multiple
**Task** : Compute the least common multiple of two positive integers. <br/>
**Input** : Two positive integers 1 <= a, b <= 2x10^9. <br/>
**Output** : The least common multiple of a and b.

## Problem 7 : Fibonacci Number Again
**Task** : Compute the n-th Fibonacci number modulo m. <br/>
**Input** : Integers 0 <= n <= 10^18 and 2 <= m <= 10^5. <br/>
**Output** : n-th Fibonacci number modulo m.

## Problem 8 : Last Digit of the Sum of Fibonacci Numbers
**Task** : Compute the last digit of F0 + F1 + ... + Fn. <br/>
**Input** : An integer 0 <= n <= 10^18. <br/>
**Output** : The last digit of F0 + F1 + ... + Fn.

## Problem 9 : Last Digit of the Partial Sum of Fibonacci Numbers
**Task** : Compute the last digit of Fm + Fm+1 + ... + Fn. <br/>
**Input** : An integer 0 <= m <= n <= 10^18. <br/>
**Output** : The last digit of Fm + Fm+1 + ... + Fn.

## Problem 10 : Sorting Problem
**Task** : Sort a sequence of numbers into nondecreasing order. <br/>
**Input** : A sequence of n numbers <a1, a2, ..., an> <br/>
**Output** : A permutation (reordering) <b1, b2, ..., bn> of the input sequence such that b1 <= b2 <= ... <= bn.

## Problem 11 : Change Problem
**Task** : Convert some amount of money into given denominations, using the smallest possible number of coins. <br/>
**Input** : An integer 1 <= money <= 10^3 and an array of d denominations c = (c1, c2, ..., cd), in decreasing order of value (c1 > c2 > ... > cd). <br/>
**Output** : A list of d integers i1, i2, ..., id such that c1xi1 + c2xi2 + ... + cdxid = money, and i1 + i2 + ... + id is as small as possible.

## Problem 12 : Tower of Hanoi Problem
**Task** : Output a list of moves that solves the Towers of Hanoi. <br/>
**Input** : An integer n. <br/>
**Output** : A sequence of moves that solve the n-disk Towers of Hanoi puzzle.

## Problem 13 : Last Digit of the Sum of Squares of Fibonacci Numbers
**Task** : Compute the last digit of F0^2 + F1^2 + ... + Fn^2. <br/>
**Input** :  An integer 0 <= n <= 10^18. <br/>
**Output** : The last digit of F0^2 + F1^2 + ... + Fn^2.

## Problem 14 : Money Change
**Task** : Compute the minimum number of coins needed to change the given value into coins with denomination 1, 5, and 10. <br/>
**Input** : An integer 1 <= money <= 10^3. <br/>
**Output** : The minimum number of coins with denominations 1, 5, and 10 that changes money.

## Problem 15 : Maximizing the Value of the Loot
**Task** : Find the maximam value of items that fit into the backpack. <br/>
**Input** : The capacity of a backpack 0 <= W <= 2x10^6 as well as the weights (w1, ..., wn) and per pound prices (p1, ..., pn) of 1 <= n <= 10^3 different compounds. <br/>
**Output** : The maximum total price of items that fit into the backpack of the given capacity: i.e., the maximum value of p1xu1 + ... + pnxun such that u1 + ... + un <= W and 0 <= ui <= wi for all i.

## Problem 16 : Maximum Product of Two Sequences
**Task** : Find the maximum dot product of two sequences of numbers. <br/>
**Input** : Two sequences of 1 <= n <= 10^3 positive integers: price1, ..., pricen and clicks1, ..., clicksn. <br/>
**Output** : The maximum value of price1xc1 + ... + pricenxcn, where c1, ..., cn is a permutation of clicks1, ..., clicksn.

## Problem 17 : Covering Segments by Points
**Task** : Find the minimum number of points needed to cover all given segments on a line. <br/>
**Input** : A sequence of 1 <= n <= 10^3 segments [l1, r1], ..., [ln, rn] on a line. <br/>
**Output** : A set of points of minimum size such that each segment [li, ri] contains a point, i.e., there exists a point x such that li <= x <= ri.

## Problem 18 : Distinct Summands
**Task** : Represent a positive integer as the sum of the maximum number of pairwise distinct positive integers. <br/>
**Input** : An integer 1 <= n <= 10^9. <br/>
**Output** : The maximum k such that n can be represented as the sum a1 + ... + ak of k distinct integers.

## Problem 19 : Largest Concatenate
**Task** : Compile the largest number by concatenating the given numbers. <br/>
**Input** : A sequence of positive integers. <br/>
**Output** : The largest number that can be obtained by concatenating the given integers in some order.

## Problem 20 : Sorted Array Multiple Search
**Task** : Search multiple keys in a sorted sequence of keys. <br/>
**Input** : A sorted array k = [k0, ..., kn-1] of 1 <= n <= 10^4 distinct integers and an array Q = {q0, ..., qm-1} of 1 <= m <= 10^4 integers. <br/>
**Output** : For each qi, check whether it occurs in k.

## Problem 21 : Majority Element
**Task** : Check whether a given sequence of numbers contains an element that appears more than half of the times. <br/>
**Input** : A sequence of 1 <= n <= 10^5 integers. <br/>
**Output** : 1, if there is an element that is repeated more than n/2 times, and 0 otherwise.

## Problem 22 : Improving QuickSort
**Task** : Modify the QuickSort algorithm so that it works fast even on sequence containing many identical elements. <br/>
**Input** : A sequence of 1 <= n <= 10^5 integers. <br/>
**Output** : Sequence sorted in non-decreasing order.

## Problem 23 : Number of Inversions
**Task** : Compute the number of inversions in a sequence of integers. <br/>
**Input** : A sequence of 1 <= n <= 30000 integers a1, ..., an. <br/>
**Output** : The number of inversions in the sequence, i.e., the number of indices i < j such that ai > aj.

## Problem 24 : Points and Segments
**Task** : Given a set of points and a set of segments on a line, compute, for each point, the number of segments it is contained in. <br/>
**Input** : A list of 1 <= n <= 50000 segments and a list of 1 <= m <= 50000 points. <br/>
**Output** : The number of segments containing each point.

## Problem 25 : Closest Points
**Task** : Find the closest pair of points in a set of points on a plane. <br/>
**Input** : A list of 2 <= n <= 10^5 points on a plane. <br/>
**Output** : The minimum distance between a pair of these points.

## Problem 26 : Money Change Again
**Task** : Compute the minimum number of coins needed to change the given value into coins with denominations 1, 3, and 4. <br/>
**Input** : An integer 1 <= money <= 10^3. <br/>
**Output** : The minimum number of coins with denominations 1, 3, and 4 that changes money.

## Problem 27 : Primitive Calculator
**Task** : Find the minimum number of operations needed to get a positive integer n from 1 using only three operations: add 1, multiply by 2, and multiply by 3. <br/>
**Input** : An integer 1 <= n <= 10^6. <br/>
**Output** : The minimum number of operations "+1", "x2", and "x3" needed to get n from 1.

## Problem 28 : Edit Distance
**Task** : Compute the edit distance between two strings. <br/>
**Input** : Two strings of length at most 100. <br/>
**Output** : The minimum number of single symbol insertions, deletions, and substitutions to transform one string into the other one.

## Problem 29 : Longest Common Subsequence of Two Sequences
**Task** : Compute the longest common subsequence of two sequences. <br/>
**Input** : Two sequences of length at most 100. <br/>
**Output** : Their longest common subsequence.

## Problem 30 : Longest Common Subsequence of Three Sequences
**Task** : Compute the longest common subsequence of three sequences. <br/>
**Input** : Three sequences of length at most 100. <br/>
**Output** : Their longest common subsequence.

## Problem 31 : Maximum Amount of Gold
**Task** : Given a set of gold bars of various weights and a backpack that can hold at most W pounds, place as much gold as possible into the backpack. <br/>
**Input** : A set of 1 <= n <= 300 gold bars of integer weights w1, ..., wn and a backpack that can hold at most 1 <= W <= 10^4 pounds. <br/>
**Output** : Find a subset of gold bars of maximum total weight not exceeding W.

## Problem 32 : 3-Partition
**Task** : Partition a set of integers into three subsets with equal sums. <br/>
**Input** : A sequence of 1 <= v1, v2, ..., vn <= 30 of 1 <= 20 <= n integers. <br/>
**Output** : Check whether it is possible to partition them into three subsets with equal sums, i.e., check whether there exist three disjoint sets S1, S2, S3 is in {1, 2, ..., n} such that S1 union S2 union S3 = {1, 2, ..., n} and sum vi where i in S1 = sum vj where j in S2 = sum vk where k in S3.

## Problem 33 : Maximum Value of an Arithmetic Expression
**Task** : Parenthesize an arithmetic expression to maximize its value. <br/>
**Input** : An arithmetic expression consisting of digits as well as plus, minus, and multiplication signs. <br/>
**Output** : Add parantheses to the expression in order to maximize its value.

## Problem 34 : Sorting Problem Again
**Task** : Sort a sequence of numbers into nonincreasing order. <br/>
**Input** : A sequence of n numbers <a1, a2, ..., an> <br/>
**Output** : A permutation (reordering) <b1, b2, ..., bn> of the input sequence such that b1 >= b2 >= ... >= bn.

# --------------------------------------------------------------------------------------------------------------------------------------

# Applications of Algorithms (You can try!!!)
1. **The Human Genome Problem** : identifying all the 100,000 genes in human DNA, determining the sequences of the 3 billion chemical base pairs that make up human DNA, storing this information in databases, and developing tools for data analysis.
2. **The Internet Information Problem** : Manage and manipulate the large volume of data, including finding good routes on which the data will travel, and using a search engin to quickly find pages on which particular information resides.
3. **Secure Electronics commerce System Project** : Provide privacy of personal information such as credit card numbers, passwords, and bank statements using public-key cryptography and digital signature.
4. An oil company may wish to know where to place its wells in order to maximize its expected profit.
5. A political candidate may want to determine where to spend money buying campaign advertising in order to maximize the chances of winning an election.
6. An airline may wish to assign crews to flights in the least expensive way possible, making sure that each flight is covered and that government regulations regarding crew scheduling are met.
7. An Internet service provider may wish to determine where to place additional resources in order to serve its customer more effectively.
8. Determine the shortest route from one intersection to another for lower labor and fuel costs.
9. Find a longest common subsequence of the two base pair sequences in DNA strands.
10. List the parts in order so that each part appears before any part that uses it in mechnical desing.
11. Find the convex hull of a n points in the plane.
12. Find a discrete Fourier transform of a samples of signal.
13. Find the best Assignment of Students to Dorm Rooms.
14. Measure Similarity of Documents.
15. Understand Natural Language.
16. Identify Objects In Photographs.
17. Play Games Well.
18. Predicting Traffic Jams.
19. Producing Automatic Movie Recommendations.
20. Ranking Internet Search Results.
21. Predicting road accidents.
22. Developed a Study Rabit Populations.
23. Develop a algorithm that can win two rocks game.
24. Develop a algorithm that can win three rocks game.
