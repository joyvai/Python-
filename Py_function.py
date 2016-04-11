def bacon():
	# We create a local variable named "spam"
	# instead of changing the value of the global
	# variable "spam":
	spam = 99
	# The name "spam" now refers to the local
	# variable only for the rest of this 
	# function:
	print spam 

spam = 42 # A global variable named "spam":
print spam # 42
bacon() # Call the bacon() 
# The bacon() does not changed the global variable

print spam

