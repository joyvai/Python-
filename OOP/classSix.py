class Square:
	# side = 0 # this is a default value
	def __init__(self,x): # this is python constructor.it calls automatic.
		self.side = x
	def area(self):
		return self.side * self.side
sqr1 = Square(4) # sqr1 is Square object or square instance
print sqr1
print sqr1.area()
sqr1.side = 5
print sqr1.area()

# Namespace holo amon akta jinish jar mordo program a j nam gulo ase ta take
#instantiation means make instance.
# Here sqr1 is instantiation.
# make a class object means instantiation.
# we call class name like a function,that's why object create.
# This object we assign a variable

