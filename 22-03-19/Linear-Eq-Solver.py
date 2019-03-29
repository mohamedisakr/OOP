def solve(b, c):
    if (b == 0) and (c == 0):
        print('Many solution.')
    elif (b == 0) and (c != 0):
        print('No solution.')
    elif (b != 0) and (c != 0):
        print('One solution ', (-c/b))
    elif (b != 0) and (c == 0):
        print('One solution ', 0)


b = 5
c = 0
solve(b, c)
