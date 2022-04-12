import numpy as np
import matplotlib.pyplot as plt

def EulerStep(tau, F, x, v):
    newX = x + v * tau
    newV = v + F(x) * tau

    return newX, newV

def VerletStep(tau, F, x, v):
    newX = x + v * tau + 0.5 * F(x) * tau**2
    newV = v + 0.5 * (F(x) + F(newX)) * tau

    return newX, newV

def Simulate(x0, v0, N, tau, F, algorithm):
    x = [x0]
    v = [v0]
    t = [0]

    for i in range(N - 1):
        t.append(t[i] + tau)
        newX, newV = algorithm(tau, F, x[i], v[i])
        x.append(newX)
        v.append(newV)

    return t, x, v

def F(theta):
    return - g / l * np.sin(theta)

def Potential(x):
    return - g * l * np.cos(x)

def Energies(x, v, V):
    arrX, arrV = np.array(x), np.array(v)
    K = 0.5 * l**2 * arrV**2
    U = V(arrX)
    E = K + U

    return E, K, U

g = 9.81
l = 0.2
N = 1000
Ncycles = 3
omega = np.sqrt(g / l)
T = Ncycles * 2 * np.pi / omega
tau = T / N

theta0 = 5 * np.pi / 6
thetaDot0 = 0

t, thetaEuler, thetaDotEuler = Simulate(theta0, thetaDot0, N, tau, F, EulerStep)
t, thetaVerlet, thetaDotVerlet = Simulate(theta0, thetaDot0, N, tau, F, VerletStep)

EEuler, KEuler, UEuler = Energies(thetaEuler, thetaDotEuler, Potential)
EVerlet, KVerlet, UVerlet = Energies(thetaVerlet, thetaDotVerlet, Potential)

fig, ax = plt.subplots()

ax.plot(t, thetaEuler, label = "Euler - $\\theta$")
ax.plot(t, thetaDotEuler, label = "Euler - $\dot{\\theta}$ [s$^{-1}$]")

ax.set_xlabel("$t$ [s]")
ax.set_ylabel("f(t)")
ax.legend()

fig1, ax1 = plt.subplots()
ax1.plot(t, thetaVerlet, label = "Verlet - $\\theta$")
ax1.plot(t, thetaDotVerlet, label = "Verlet - $\dot{\\theta}$ [s$^{-1}$]")

ax1.set_xlabel("$t$ [s]")
ax1.set_ylabel("f(t)")
ax1.legend()

fig2, ax2 = plt.subplots()
ax2.plot(t, thetaEuler, label = "Euler - $\\theta$")
ax2.plot(t, thetaVerlet, label = "Verlet - $\\theta$")

ax2.set_xlabel("$t$ [s]")
ax2.set_ylabel("$\\theta(t)$")
ax2.legend()

fig3, ax3 = plt.subplots()
ax3.plot(t, thetaDotEuler, label = "Euler - $\dot{\\theta}$")
ax3.plot(t, thetaDotVerlet, label = "Verlet - $\dot{\\theta}$")

ax3.set_xlabel("$t$ [s]")
ax3.set_ylabel("$\dot{\\theta}(t)$ [s$^{-1}$]")
ax3.legend()

fig4, ax4 = plt.subplots()
ax4.plot(t, EEuler, label = "Energia totale - Eulero")
ax4.plot(t, KEuler, label = "Energia cinetica - Eulero")
ax4.plot(t, UEuler, label = "Energia potenziale - Eulero")

ax4.set_xlabel("$t$ [s]")
ax4.set_ylabel("$E$ [N m]")
ax4.legend()

fig5, ax5 = plt.subplots()
ax5.plot(t, EVerlet, label = "Energia totale - Verlet")
ax5.plot(t, KVerlet, label = "Energia cinetica - Verlet")
ax5.plot(t, UVerlet, label = "Energia potenziale - Verlet")

ax5.set_xlabel("$t$ [s]")
ax5.set_ylabel("$E$ [N m]")
ax5.legend()

plt.show()