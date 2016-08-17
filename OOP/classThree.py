class Point:
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y 
	def __del__(self):
		class_name = self.__class__.__name__
		print class_name, "destroyed"

pt1 = Point()
pt2 = pt1 # pt2 = Point()
pt3 = pt1 # pt3 = Point()
print id(pt1), id(pt2),id(pt3) 
del pt1 
del pt2
del pt3



class AnotherPoint:
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y
	def __del__(self):
		class_name_one = self.__class__.__name__
		print class_name_one, " destroyed"
pt1 = AnotherPoint()
print id(pt1)
del pt1		



