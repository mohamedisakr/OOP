import math

def SolveQuadratic(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if (d < 0):
        print('No solution')
        return False
    else: #(d == 0):
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(x1, ' ', x2)
        return True


a = 1
b = 2#-3
c = 4#2
hasSolution = SolveQuadratic(a, b, c)
print(hasSolution)
