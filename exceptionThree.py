
def divide(x, y):
	try:
		result = x / y
		print result
	except ZeroDivisionError:
		print "Division by Zero!"
	except TypeError:
		print 'Unsupported operand type.'
	else:
		print 'result is ',result
	finally:
		print "executing finally clause."
d = divide(2,1)
print d
e = divide(2,0)
print e
print divide('a','b')
