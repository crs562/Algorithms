# Uses python3

"""
FibRecurs(n):
    if n <= 1:
        return n
    else:
        return FibRecurs(n-1) + FibRecurs(n-2)
----------------------------------------------
FibList(n):
    create an array F[0...n]
    F[0] <- 0
    F[1] <- 1
    for i from 2 to n:
        F[i] <- F[i-1] + F[i-2]
    return F[n]
"""

# Gives Correct Ans untill Fib(71)
def FibByFormula1(n):
    fibn1 = (1+math.sqrt(5))/2 
    fibn2 = (1-math.sqrt(5))/2
    fibn = (1/math.sqrt(5))*(math.pow(fibn1, n) - math.pow(fibn2, n))
    return int(fibn)

# not efficient algorithms
def FibByFormula2(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return int(math.pow(2, 0.694*n))

# not efficient algorithms
def FibByFormula3(n):
    if n <= 1:
        return n
    else:
        return int(math.pow(1.6, n))

def FibRecurs(n):
    if n <= 1:
        return n
    else:
        return fibNaive(n-1) + fibNaive(n-2)

def FibList(n):
    f = []
    f.append(0)
    f.append(1)
    for i in range(2, n+1):
        temp = f[i-1] + f[i-2]
        f.append(temp)
    return f[n]

# Still getting some error getting -ve value
def FibByMatrix(n):
    if n <= 1:
        return n
    base = np.array([[0, 1],
                     [1, 1]])
    mulMatrix = np.array([0, 1])
    nPower = matrix_power(base, n)
    print(n, nPower)
    finalMatrix = np.matmul(nPower, mulMatrix)
    return finalMatrix[0]

def StressTest(N):
    for i in range(0, N+1):
        result1 = FibRecurs(i)
        result2 = FibList(i)
        #print("result1: ", result1, "result2: ", result2)
        if result1 == result2:
            print(i, "OK")
        else:
            print("Wrong answer: ", result1, result2)
            return 0

##for i in range(0, 100):
##    print(FibByMatrix(i))
#StressTest(100)

n = int(input())
print(FibList(n))
