class Rectangle:
	def __init__(self):
		print 'Inside init of Rectangle'
	def area(self,x,y):
		return x * y
class Square(Rectangle):
	def __init__(self):
		print 'Inside init of Square'
	def area(self,x):
		return x * x
sq = Square()
print sq.area(5)

# if we make method in subclass which name is same in Base class Method Name
# then we can make subclass object and then using object we call this method
# then subclass method are fired.This is called method overriding.
