# lambda is key word which is used for annonymous function.
# Small anonymous functions can be created with the lambda keyword
def make_incrementor(n):
	return lambda x:x+n

f = make_incrementor(42)
print f(0)
print f(2)

a.sort(key = lambda pair: pair[0])
print a
