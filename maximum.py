# This is a python program
# def means here defination.This is a function keyword.In C language we start void.
# after def we define function name.Here maxFunction is function name
# then we define a local variable named largest_so_far = -1
# a is list .list like array.it stores the value.
# then you use php for loop.This for loop different from 
# other programming languages.
# I just show you the simulation
# In for loop the_num is looping variable
# the_num stores list or array value.
# the_num = 9,41,12,3,74,15
# if 9 > -1 : which is True
# 9 is a largest_so_far
# Then 41 > 9: which is True
# 41 is a largest_so_far
# 12 > 41: False
# 41 still largest_so_far
# 3 > 41: False
# 41 still largest_so_far
# 74 > 41:True
# now largest_so_far 74
# 74 > 15:True
# so the final answer is 74
def maxFunction():
	largest_so_far = -1 
	print 'Before',largest_so_far
	a = [9,41,12,3,74,15]
	for the_num in a:
		if the_num > largest_so_far:
			largest_so_far = the_num
		print largest_so_far,the_num
print 'After',largest_so_far
