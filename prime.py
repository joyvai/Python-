def is_prime():

	number = int(raw_input("Enter a number:"))

	if number > 1:
		for i in range (2,number-1):
			if number-1 % i == 0:
				return False
		else:
			return True
	else:
		return False

print is_prime()