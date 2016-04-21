# A simple example class
# How to define a class
# At first declare "class" keyword
# Then write the class name it was anything but meaningful
# After writing class name give the colon

class MyClass:
	i = 12345
	def f(self):
		name = raw_input("Enter your name: ")
		age = raw_input("Enter your age: ")
		return 'Hi '+ name +' so your age is ' + age
	def __init__(self,realpart,imagpart):
		self.r = realpart
		self.i = imagpart

# a is class instantiation
# create a new instance of the class and assigns this object to the local variable x.
a = MyClass(3.0,-4.5)
print a.f()
print a.r, a.i
