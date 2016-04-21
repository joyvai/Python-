class Dog:
	tricks = []
	def __init__(self,name):
		self.name = name
		self.tricks.append(name)
		
	def add_trick (self,trick):
		self.tricks.append(trick)

d = Dog('dula')
e = Dog('kuyr')
d.add_trick('rool over')
e.add_trick('tommy')
print e.tricks
print d.tricks
