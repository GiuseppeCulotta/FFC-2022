from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt
from vec2d import vec2d
from integrator import integrator
import scipy.constants as spc
from scipy.optimize import curve_fit

def F(r : vec2d, F0):
    return F0 * r / r**3

Z1, Z2 = 2, 79                      # Atomic number of alpha and Au
Q1, Q2 = Z1 * spc.e, Z2 * spc.e     # Charges of the alpha and Au particles in C
alphaMass = 2 * spc.proton_mass + 2 * spc.neutron_mass
                                    # Alpha particle mass in kg

E = 5e6 * spc.electron_volt         # Initial energy of the alpha particle in J
F0 = Q1 * Q2 / (4 * np.pi * spc.epsilon_0 * alphaMass)
                                    # Constant in front of r**2 (N * m^2)

d0 = F0 / E * alphaMass             # Typical length scale of the problem (N * m^2 / J = m),
                                    # ~ minimum distance between particle and Au atom

Npart = 500
offset = 100
theta = np.zeros(Npart)
np.random.seed()
xList = []

solver = integrator()

for i in range(Npart):
    x0 = vec2d(- offset * d0, 2 * offset * (np.random.rand() - 0.5) * d0 / 10)
    v0 = vec2d(np.sqrt(2 * E / alphaMass), 0)

    tau = d0 / v0.mod()
    N = int(2 * x0.mod() / d0)

    t, x, v = solver.Solve(x0, v0, tau, N, lambda x: F(x, F0))

    theta[i] = v0.GetAngle(v[-1])

    if(i < 10):
        xList.append(x)

fig, ax = plt.subplots()

for traj in xList:
    ax.plot([vec.GetX() / d0 for vec in traj], [vec.GetY() / d0 for vec in traj], label = "Data")
ax.plot([0], [0], label = "Centro diffusivo", marker = ".")
ax.set_xlabel("$x / d_0$")
ax.set_ylabel("$y / d_0$")

fig1, ax1 = plt.subplots()
nbins = 50
ax1.hist(theta, histtype = "step", bins = nbins, label = "Data", range = (0, np.pi))
ax1.set_yscale("log")
ax1.set_xlabel("$\\theta$")
ax1.set_ylabel("Counts")

vals = [0, np.pi / 6, np.pi / 3, np.pi / 2, np.pi * 2 / 3, 5 * np.pi / 6, np.pi]
keys = ["0", "$\pi / 6$", "$\pi / 3$", "$\pi / 2$", "$2\pi / 3$", "$5\pi / 6$", "$\pi$"]
ax1.set_xticks(vals, keys)



def fit(theta, norm, exp):
    return norm / np.sin(theta / 2)**exp

counts, bins = np.histogram(theta, bins = nbins)
bins = bins[1:] - (bins[1] - bins[0]) / 2
pars, cov = curve_fit(fit, bins, counts, p0 = [counts[-1], 2], sigma = counts)

ax1.plot(bins, fit(bins, pars[0], pars[1]))
print(pars)

plt.show()
