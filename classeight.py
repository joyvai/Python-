class Dog:
	kind = 'canine' # class variable shared by all instances
	kind = 'Kala kutta'
	def __init__(self, name):
		self.name = name # instance variable unique to each instance
d = Dog('Fido')
e = Dog('Buddy')
print d.kind # shared by all dogs
print e.kind # canine
print d.name # Fido .unique to d
print e.name # unique to e
