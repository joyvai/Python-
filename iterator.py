class Reverse:
	"""Iterator for looping over a sequence backwards."""
	# When we make a class iterable this time we keep focus or implement
	# two function which is __init__ and __iter__
	def __init__(self, data):
		self.data = data
		self.index = len(data)

	def __iter__(self): #when self call,this time class had iterable
		return self

	def next(self): # when stopIteration exception raise this method told you.
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]
rev = Reverse('ABCD') # here rev is not a string.
print rev 
for i in rev:
	print i
