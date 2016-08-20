class Rectangle:
	def __init__(self):
		print 'Inside init of rectangle'
class Square(Rectangle):
	pass
r = Rectangle()
sqr = Square()
#output => Inside init of rectangle
#          Inside init of rectangle
