#!~/usr/bin/python3

'''
Reference: 
Introduction to Computation and Programming Using Python
https://python-forum.io/Thread-John-Guttag-Python-Book-Finger-Exercise-5
'''
'''
Question: Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user.
'''

integer = int(input("Enter Integer: "))
pwr = 1
while pwr < 6:
	if integer < 0:
		root = x
	else:
		root = 0

	while root ** pwr <= integer:
		if root ** pwr == integer:
			print(root, " ** ", pwr, "=", integer)
		else:
			if integer ** 1 != integer:
				print(integer, "No such integer pair exists.")
		root += 1
	pwr += 1
