catNames = []
while True:
	print 'Enter the name of cat ' + str (len(catNames)+1) +' or enter nothing to stop.'
	name = raw_input()
	if name == '':
		break
	catNames = catNames + [name] # list concatenation
	print 'The cat names are:'
for name in catNames:
	print ' ' + name
	

