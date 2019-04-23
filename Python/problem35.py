# Use Python 3

"""
LinearSearch(A, v):
    index = NIL
    for i = 1 to A.length
        if A[i] == v:
            index = i
"""

def LinearSearch(A, v):
    index = None
    for i in range(0, len(A)):
        if A[i] == v:
            return i
    return index

A = [31, 41, 59, 26, 41, 58]
print(LinearSearch(A, 1))
print(LinearSearch(A, 31))
print(LinearSearch(A, 41))
print(LinearSearch(A, 58))
