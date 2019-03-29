'''
A year is leap year if the following conditions are satisfied:
1) Year is multiple of 400.
2) Year is multiple of 4 and not multiple of 100.
'''

# Python program to check leap year or not

def IsLeapYear(year):
    if (((year % 4) == 0) and ((year % 100) != 0)) or ((year % 400) == 0):
        return True
    else:
        return False


def GenerateCommonYear(start, end):
	for i in range(start, end+1):
		for j in range(1, 4):
			print(start+j)
			

# test
count = 0
line = ''
with open('Leap-Year.txt', 'r+') as f:
    for line in f.readlines():
        if(IsLeapYear(int(line))): 
            print(line + ' ' +  ' : Leap Year')
            count += 1
        else: 
            print("Not a Leap Year")
        #print(line)

print('# of leap years ', count)

print(IsLeapYear(2001))

'''
def IsLeapYear(year): 
    if (year % 4) == 0: 
        if (year % 100) == 0: 
                if (year % 400) == 0: 
                    return True
                else: 
                    return False
        else: 
            return True
    else: 
        return False
'''	

'''        
#year = 2019 #2000
if(checkYear(year)): 
	print("Leap Year") 
else: 
	print("Not a Leap Year")
'''
