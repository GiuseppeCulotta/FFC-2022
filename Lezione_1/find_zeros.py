import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

def TimeIt(f, args, string):
    start = dt.datetime.now()
    values = f(*args)
    end = dt.datetime.now()

    print(string.format(values))
    print(f"Computation time: {(end - start).microseconds} us")

def f(x):
    return np.log(x)

def FindZero(a, b, minPrec, method = "bisect"):
    fa, fb = f(a), f(b)
    if(fa * fb > 0): 
        print("Invalid interval. Please try again. Returning -1000.")
        return -1000

    m = a

    if(method == "lin"):
        m = (b * fa - a * fb) / (fa - fb)
    elif(method == "rand"):
        m = np.random.rand() * (b - a) + a
    else:
        m = (a + b) / 2

    fm = f(m)

    if(fm == 0 or np.abs(fm) < minPrec): return m
    if(fa * fm < 0): return FindZero(a, m, minPrec)
    if(fb * fm < 0): return FindZero(m, b, minPrec)

np.random.seed()


TimeIt(FindZero, (0.1, 3.05, 1e-4, "bisect"), "Zero found at: {}")
TimeIt(FindZero, (0.1, 3.05, 1e-4, "lin"), "Zero found at: {}")
TimeIt(FindZero, (0.1, 3.05, 1e-4, "rand"), "Zero found at: {}")
