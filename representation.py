for x in range(1, 11):
	print repr(x).rjust(2),repr(x*x).rjust(3),repr(x**3).rjust(4)
for x in range(2,21):
	print '{0:2d} {1:3d} {2:4d}'.format(x,x**2,x**3)
