def ConvertToBytesOrKilobytes(n, flag):
    if (flag == 'b' or flag == 'B'):
        result = n 
    elif (flag == 'k' or flag == 'K'):
        result = n * 1024
    return result


n  = int(input('Type a number to convert : '))
flag = input('b for bytes, k for kilobytes : ')
print(ConvertToBytesOrKilobytes(n, flag))
