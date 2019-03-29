def IsValid(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else :
        return False

    
def IsEquilateral(a, b, c):
    if(a == b) and (a == c):
        return True
    else:
        return False


def IsIsosceles(a, b, c):
    if(a == b and a != c) or (b == c and b != a) or (a == c and a != b):
        return True
    else:
        return False

def IsScalene(a, b, c):
    if (a != b) and (b != c) and (a != c):
        return True
    else:
        return False


def IsRight(a, b, c):
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return True
    else:
        return False    

'''
a = 2#10
b = 12
c = 7#13
#print('Equilateral' if(IsEquilateral(a, b, c)) else 'Not equilateral')
#print('Isosceles' if(IsIsosceles(a, b, c)) else 'Not isosceles')
#print('Scalene' if(IsScalene(a, b, c)) else 'Not Scalene')
'''
'''
a = 5#1
b = 12#10
c = 13#12
print('Valid Triangle' if(IsValid(a, b, c)) else 'Not valid triangle')

print('Right Triangle' if(IsRight(a, b, c)) else 'Not right triangle')
# min = a if a < b else b
'''
