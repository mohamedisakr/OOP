import math

def IsPointBelongToCircle(x, y, r):
    if (math.sqrt((x**2) + (y**2)) <= r):
        return True
    else:
        return False

# x = 4, y = 4, r = 6
# x = 3, y = 3, r = 2
# x = 6, y = 6, r = 6
