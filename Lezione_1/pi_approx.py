import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy.optimize import curve_fit
import datetime as dt

def ApproximatePi(N):
    n = 0
    # Compute random x and y coordinates
    x = np.random.random(N)
    y = np.random.random(N)
    # Compute radii
    r2 = x**2 + y**2

    # Count how many points lay in the circle
    for rSq in r2:
        if rSq < 1:
            n += 1

    return n, x, y

piList = []; NList = range(10000, 1000000, 100000)
start = dt.datetime.now()
for N in NList:
    # Set random seed
    np.random.seed()

    n, x, y = ApproximatePi(N)
    piList.append(4 * n / N)

    # Draw circle 
    circleX = np.linspace(0, 1, 1000)
    circleY = np.sqrt(1 - circleX**2)

    if N == 10000:
        # Draw plot
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth = 0, marker = ".", markersize = 5, label = "data")
        ax.plot(circleX, circleY)
        ax.add_patch(patches.Rectangle((0, 0), 1, 1, linewidth = 1, edgecolor = 'r', facecolor = 'none'))

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.axis("equal")
end = dt.datetime.now()
print(f"Computation time: {(end - start).microseconds} ms")

fig1, ax1 = plt.subplots()
ax1.plot(NList, piList, label = "Computed")
ax1.hlines(np.pi, NList[0], NList[-1], label = "Exact")
ax1.set_xlabel("N")
ax1.set_ylabel("$\pi$")

def f(N, A, B):
    return A / N**B

p, cov = curve_fit(f, NList, np.abs(np.array(piList) - np.pi), p0 = [0.02 * NList[0] * np.abs(np.array(piList) - np.pi)[0], 1 / 2])

fig2, ax2 = plt.subplots()
ax2.plot(NList, np.abs(np.array(piList) - np.pi), linewidth = 0, marker = ".", label = "Computed")
ax2.plot(NList, f(np.array(NList), p[0], p[1]))
print(f"A = {p[0]},\tB = {p[1]}")
ax2.set_xlabel("N")
ax2.set_ylabel("$\pi$")

plt.show()