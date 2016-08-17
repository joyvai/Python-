class Employee:
	# Here Employee is a base class
	empCount = 0 # global variable
	
	def __init__(self,name,salary,age): # __init__ is class constructor or initialization method
	#python call this method when you create new instance of this class
	
		self.name = name
		self.salary = salary
		self.age = age 
		Employee.empCount += 1
		
	def displayCount (self):
		print "Total Employee %d" % Employee.empCount
		
	def displayEmployee(self):
		print "Name: ",self.name, ", Salary: ", self.salary , ", Age: ",self.age
		
"This would create first object of Employee class"
emp1 = Employee("Zara",20000,7)
#second object
emp2 = Employee("Manni",60000,98)
"Accessing attribute"
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount 
print hasattr(emp1,'age') # Returns true if 'age' attribute exists
print getattr(emp2,'age') 
setattr(emp1,'age',999)
print getattr(emp1,'age')

