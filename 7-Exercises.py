'''
## (7) Print the product of digits of first number
a = open('1.txt', 'r').read().split()
n = int(a[0])
p = 1
while n > 0:
    p *= n % 10
    n //= 10
print(p)    
'''

'''
## (6) Print the first number in reverse order
a = open('1.txt', 'r').read().split()
##n = str(a[0])
##print(n[::-1])

n = int(a[0])
b = 0
while n > 0:
    d = n % 10
    b = b * 10 + d
    n //= 10
print(b)    
'''

'''
## (5) Print the sum of the digits of the first number from the file.
a = open('1.txt', 'r').read().split()
n = int(a[0])
num = n
s = 0
while n > 0:
    s += n % 10
    n //= 10
print(num, s)    
'''

'''
## (4) Print the number of digits of the second number from the file.
a = open('1.txt', 'r').read().split()
##n = str(a[1])
##print(n, len(n))

n = int(a[1])
num = n
count = 0
while n > 0:
    count += 1
    n //= 10
print(num, count)    

'''

'''
## (3) Find out if the first number in the file is Prime number
a = open('1.txt', 'r').read().split()
n = int(a[0])
r = int(n ** 0.5)
k = 2
while k < r+1:
    if n % k == 0:
        print(n , ' is not prime')
        break
    k += 1
else:
    print(n, ' is prime')
'''

'''
## (2)  Find out if the first number is a power of the second number
a = open('1.txt','r').read().split()
first = int(a[0])
second = int(a[1])
print(first, second)
if first % second == 0:
    print('YES')
else:
    print('NO')
'''

'''
## (1) list all factors
a = open('1.txt', 'r').read().split()
n = int(a[0])
print(1, end=' ')
for i in range(2, n//2):
    if n % i == 0:
        print(i, end=' ')
print(n , end=' ')
'''
