def gen(n):
	i = 0
	while i < n:
		yield i
		i = i + 1
x = gen(5)
print x
for item in x:
	print item
