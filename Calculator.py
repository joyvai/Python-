# Program make a simple calculator that can add,subtract,Multiply,divison

# define functions

def add(x,y):
	"""This function adds two numbers."""
	return x + y
def subtract (x,y):
	"""This function subtract two numbers."""
	return x - y
def multiply (x,y):
	"""This function multiplies two numbers."""
	return x * y
def divide (x,y):
	return x / y

# take input from the user
print 'Select Operation.'
print '1.Add'
print '2.Subtract'
print '3.Multiply'
print '4.Divide'

choice = raw_input ("Enter choice(1/2/3/4): ")
num1 = int (raw_input("Enter first Number: "))
num2 = int(raw_input("Enter second Number: "))

if choice == '1':
	print num1, '+' ,num2, '=', add(num1,num2)

elif choice == '2':
	print num1, '-' , num2, '=',subtract(num1,num2)

elif choice == '3':
	print num1, '*' , num2, '=',multiply(num1,num2)
elif choice == '4':
	print num1, '/' , num2, '=',divide(num1,num2)
else:
	print 'Invalid Input'  

