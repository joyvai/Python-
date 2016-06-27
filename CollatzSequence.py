
def collatz(number):
	if number % 2 == 0:
		return 'even number %d'%	number
	else:
		a = 3 * number + 1
		return a

userType = int(raw_input('Give me a number '))
print collatz(userType) 
