import numpy as np

class integrator:
    def __init__(self, method : str = "Verlet"):
        if(method == "Euler"):
            self.method = self.MakeStepEuler
        elif(method == "Verlet"):
            self.method = self.MakeStepVerlet
        else:
            exceptionString = "Please, specify a method. The implemented ones are:\n"
            exceptionString += "Euler\nVerlet"
            raise Exception(exceptionString)

    def SetMethod(self, method : str = None):
        if(method == "Euler"):
            self.method = self.MakeStepEuler
        elif(method == "Verlet"):
            self.method = self.MakeStepVerlet
        else:
            exceptionString = "Please, specify a method. The implemented ones are:\n"
            exceptionString += "Euler\nVerlet"
            raise Exception(exceptionString)

    def MakeStepEuler(self, x0, v0, tau, F):
        x = x0 + v0 * tau
        v = v0 + F(x0) * tau
        return x, v

    def MakeStepVerlet(self, x0, v0, tau, F):
        x = x0 + v0 * tau + 0.5 * F(x0) * tau**2
        v = v0 + 0.5 * (F(x0) + F(x)) * tau
        return x, v

    def Solve(self, x0, v0, tau, N, F):
        tList, xList, vList = [0], [x0], [v0]

        for i in range(N - 1):
            x, v = self.method(xList[i], vList[i], tau, F)
            tList.append(tList[i] + tau)
            xList.append(x)
            vList.append(v)

        return np.array(tList), np.array(xList), np.array(vList)
