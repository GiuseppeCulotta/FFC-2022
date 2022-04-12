import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

def Condition(sum, oldSum, prec):
    return np.abs(sum - oldSum) / sum > prec

def f(x, n):
    return x**n

def SumUpToN(x, N):
    sum = 0
    for i in range(N):
        sum += f(x, i)

    return sum

def SumUpToPrec(x, prec):
    sum = 1; i = 1
    oldSum = 0
    

    while(Condition(sum, oldSum, prec)):
        oldSum = sum
        sum += f(x, i)
        i += 1

    return sum

start = dt.datetime.now()
sum = SumUpToN(0.9999, 10000)
end = dt.datetime.now()
print(f"Fixed N. Computation time: {(end - start).microseconds/1000:1.3f} ms,\tSum: {sum:1.1f}")

start = dt.datetime.now()
sum = SumUpToPrec(0.9999, 1e-6)
end = dt.datetime.now()
print(f"Fixed precision. Computation time: {(end - start).microseconds/1000:1.3f} ms,\tSum: {sum:1.1f}")