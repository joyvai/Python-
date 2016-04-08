# create a empty list 
CatNames = []
while True:
	print "Enter the name of cat" + str(len(CatNames)+1)+'Or enter nothing to stop:'
	name = raw_input()
	if name == '':
		break
	CatNames = CatNames + [name]
	print "The cat names are:"
	for name in CatNames:
		print ' '+name	