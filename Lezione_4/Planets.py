from socket import MsgFlag
import numpy as np
import matplotlib.pyplot as plt
from vec2d import vec2d
from integrator import integrator
import scipy.constants as scc

G = 6.67e-11 / scc.astronomical_unit**3 * scc.year**2      # AU^3 / kg year**2
Msun = 1.988e30                                            # kg

a0 = vec2d(0.307499, 0)                                    # AU
v0 = 58.98 * 1e3 / scc.astronomical_unit * scc.year        # AU / year
v0 = vec2d(0, - v0)
N = 10000
T = 0.241                                                  # year
tau = 3 * T / N                                                # year
alpha = 0.0

def F(r : vec2d):
    return - G * Msun / r**3 * (1 + alpha / r.mod()) * r

def GetEnergyAndAngMom(positions, velocities):
    E = np.zeros(len(positions))
    L = np.zeros(len(positions))
    for i in range(len(positions)):
        T = 0.5 * velocities[i]**2
        V = - G * Msun / positions[i].mod() * (1 + alpha / (2 * positions[i].mod()))
        E[i] = T + V
        L[i] = positions[i].mod() * velocities[i].mod() * np.sin(positions[i].GetAngle(velocities[i]))
    return E, L


solver = integrator()

tMerc, possMerc, vMerc = solver.Solve(a0, v0, tau, N, F)

x, y = [pos.GetX() for pos in possMerc], [pos.GetY() for pos in possMerc]
E, L = GetEnergyAndAngMom(possMerc, vMerc)

print(f"Mean E = {np.mean(E):1.15f}, Error = {np.std(E):1.15f}")
print(f"Mean L = {np.mean(L):1.15f}, Error = {np.std(L):1.15f}")

# Compute eccentricity
ra, rp = np.max([pos.mod() for pos in possMerc]), np.min([pos.mod() for pos in possMerc])
e = (ra - rp) / (ra + rp)
print(f"e = {e:1.4f}")

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot([0], [0], marker = "x")
ax.axis("equal")
ax.set_xlabel("x (AU)")
ax.set_ylabel("y (AU)")

fig2, ax2 = plt.subplots()
ax2.plot(tMerc, L)
ax2.set_xlabel("t (years)")
ax2.set_ylabel("$L / M_{Merc} (AU^2/year)$")

fig3, ax3 = plt.subplots()
ax3.plot(tMerc, E)
ax3.set_xlabel("t (years)")
ax3.set_ylabel("$E / M_{Merc} (AU^2/year^2)$")

plt.show()