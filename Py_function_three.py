
def just_A_function():

	while True:

		try:

			a = int(raw_input('Enter first number: '))
			b = int (raw_input('Enter second number: '))
			if a > b:
				print '%d is greater than %d' %(a,b)
				print '%d is a maxmimum number' %a
				break
			elif a < b:
				print '%d is less than %d' %(a,b)
				print '%d is a maxmimum number' %b
				break
			elif a == b:
				print '%d is equal to %d' %(a,b)
				break

		except ValueError:
			print "Oops baby!This is a wrong number.You have to use integer number baby!!"
	
just_A_function()
