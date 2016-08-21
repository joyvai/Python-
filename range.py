print range(5,10) #[5,6,7,8,9]
print range(0,10,3) # [3,6,9]

# Here third argument increase the value
# at first 0+3 = 3 => 3 + 3 = 6 => 6+3=9
# 10 is a condition like stop point when reach 10 stop the program
print range(-10, -100, -30)
# [-10, -40, -70]

a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
	print i, a[i]
	
for n in range(2, 10):
	for x in range(2, n):
		if n % 2 == 0:
			print n, 'equals',x,'*',n/x
			break
	else:
		print n, 'is a prime number'
