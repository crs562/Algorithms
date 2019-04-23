# Use Python 3

"""
InsertionSort(A):
    for j = 2 to A.length:
        key = A[j]
        // Insert A[j] into the sorted sequence A[1...j-1].
        i = j - 1
        while i > 0 and A[i] < key
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
"""

def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] < key:
            print("Swapped {} for {}".format(A[j], A[i]))
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key    
    return A

A = [5, 2, 4, 6, 1, 3]
print(InsertionSort(A))

A = [31, 41, 59, 26, 41, 58]
print(InsertionSort(A))


