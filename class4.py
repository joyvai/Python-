class Bag:
	def __init__(self):
		self.data = []
	def add(self,x):
		self.data.append(x)
	def addTwice(self,x):
		self.add(x) #  addTwice call add method
		self.add(x)
a = Bag()
print a
a.add('joy')
a.addTwice(2)
print a.data
