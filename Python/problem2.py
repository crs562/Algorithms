# Uses python3

import random

"""
MaxPairwiseProductNaive(A[1...n]):
    product <- 0
    for i from 1 to n:
	for j from 1 to n:
            if i != j:
		if product < A[i]*A[j]:
                    product <- A[i]*A[j]
    return product
------------------------------------------
MaxPairwiseProductNaive(A[1...n]):
    product <- 0
    for i from 1 to n:
	for j from i+1 to n:
            product <- max(product, A[i]*A[j]
    return product
-------------------------------------------
MaxPairwiseProductFast(A[1...n]):
    index1 <- 1
    for i from 2 to n:
	if A[i] > A[index1]:
            index1 <- i
    if index1 = 1:
	index2 <- 2
    else:
	index2 <- 1
    for i from 1 to n:
	if i != index1 and A[i] > A[index2]:
            index2 <- i
    return A[index1]*A[index2]
-----------------------------------------------
MaxPairwiseProductFast(A[1...n]):
    index <- 1
    for i from 2 to n:
    if A[i] > A[index]:
        index <- i
    swap A[index] and A[n]
    index <- 1
    for i from 2 to n-1:
        if A[i] > A[index]:
            index <- i
    swap A[index] and A[n-1]
    return A[n-1]*A[n]
--------------------------------------------------
MaxPairwiseProductFast(A[1...n]):
    sort(A)
    return A[n-1]*A[n]
------------------------------------------------
StressTest(N, M):
    while true:
        n <- random integer between 2 and N
	allocate array A[1...n]
	for i from 1 to n:
            A[i] <- random integer between 0 and M
	    print(A[1...n])
	    result1 <- MaxPairwiseProductNaive(A)
	    result2 <- MaxPairwiseProductFast(A)
	    if result1 = result2:
                print("OK")
	    else:
		print("Wrong answer: ", result1, result2)
		return
"""

def MaxPairwiseProductNaive(a, n):
    product = 0
    for i in range(0, n):
        for j in range(i+1, n):
            temp = a[i]*a[j]
            if temp > product:
                product = temp
    return product

def MaxPairwiseProductFast1(a, n):
    index1 = 0
    for i in range(1, n):
        if a[i] > a[index1]:
            index1 = i
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0
    for j in range(0, n):
        if j != index1 and a[j] > a[index2]:
            index2 = j
    print(index1, index2)
    return a[index1]*a[index2]

def MaxPairwiseProductFast2(a, n):
    index = 0
    for i in range(1, n):
        if a[i] > a[index]:
            index = i
    a[index], a[n-1] = a[n-1], a[index]
    #print(a)
    index = 0
    for j in range(1, n-1):
        if a[j] > a[index]:
            index = j
    a[index], a[n-2] = a[n-2], a[index]
    #print(a)
    return a[n-2]*a[n-1]

def MaxPairwiseProductFast3(a, n):
    a.sort()
    return a[n-2]*a[n-1]

def StressTest(N, M):
    while True:
        n = random.randint(2, N+1)
        a = []
        for i in range(0, n):
            a.append(random.randint(0, M+1))
        print(a)
        result1 = MaxPairwiseProductNaive(a, n)
        result2 = MaxPairwiseProductFast2(a, n)
        if result1 == result2:
            print("OK")
        else:
            print("Wrong answer: ", result1, result2)
            return 0

    
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)
#print(MaxPairwiseProductNaive(a))
#n = 2
#a = [100000, 90000]
print(MaxPairwiseProductFast3(a, n))

#StressTest(5, 9)
