def digit_sum(n):
	Sum = 0
	while n > 10:
		Sum = Sum + (n % 10)
		n = n // 10

	return Sum + n
	
print digit_sum(1234)
