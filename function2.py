def spam (divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		return 'Error: Invalid Argument'
print spam (2)
print spam (42)
print spam(0)
print spam(1)

