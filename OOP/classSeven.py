class Family:
	def __init__(self,religion,member,title):
		self.title = title
		self.member = member
		self.religion = religion
	def show(self):
		print self.religion,self.member,self.title

fam1 = Family(raw_input('Enter your religion: '),raw_input("Enter your family member"),raw_input('Enter family title'));
show =fam1.show()
print type(show)
print show
