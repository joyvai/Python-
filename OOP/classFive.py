class A:
	def f(self):
		return self.g() # A
	def g(self):
		return 'A'
# class B inherit A
class B(A):
	def g(self):
		return 'B'
a = A()
b = B()

print a.f() #A
print b.f() # B
print a.g() # A
print b.g() #B
