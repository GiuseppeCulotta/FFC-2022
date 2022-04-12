import numpy as np

class vec2d:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # Setters
    def SetX(self, x):
        self.x = x
    
    def SetY(self, y):
        self.y = y

    # Getters
    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    # Operators definitions
    def __pos__(self):
        return self

    def __neg__(self):
        return vec2d(- self.x, - self.y)

    def __add__(self, other):
        return vec2d(self.x + other.GetX(), self.y + other.GetY())

    def __sub__(self, other):
        return self + (- other)

    def __mul__(self, other):
        if(isinstance(other, vec2d)):
            return self.x * other.GetX() + self.y * other.GetY()
        return vec2d(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return vec2d(self.x / other, self.y / other)

    def __pow__(self, other):
        return self.mod()**other

    def __str__(self):
        return f"({self.x}, {self.y})"

    # Useful operations
    def mod(self):
        return np.sqrt(self.x**2 + self.y**2)

    def unit(self):
        return self / self.mod()

    def GetAngle(self, other):
        return np.arccos(self * other / (self.mod() * other.mod()))