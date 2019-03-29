def Swap(a, b):
    if(a < b):
        a,b = b,a

def GetMax(a, b):
    if(a > b):
        return a
    else:
        return b

a = 12#3
b = 17#2
c = 11 #1

m = GetMax(GetMax(a,b), c)
print('Max is ', m)

##Swap(a, b)
##Swap(b, c)
##Swap(a, c)

##print(a, ' ', b, ' ', c)

##print(a)
##print(b)

##a = 2
##b = 12

##        temp = a #
##        a = b
##        b = temp
        
##        print('a = ', a)
##        print('b = ', b)
