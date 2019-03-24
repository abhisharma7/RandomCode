#!~/usr/bin/python3

'''
Reference: Introduction to Computation and Programming Using Python
'''

x = int(input("Enter Integer"))
ans = 0
while ans ** 3 < abs(x):
	ans = ans + 1
if ans**3 != abs(x):
	print (x, 'is not a perfect cube')
else:
	if x < 0:
		ans = -ans
	print ('Cube Root of', x, 'is', ans)
