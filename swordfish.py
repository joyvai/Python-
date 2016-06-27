while True:
	print 'Who are you?'
	name = raw_input()
	if name != 'Joe':
		continue
	print 'Hello,Joe.What is the password?(It is a fish.)'
	passWord = raw_input('Give your password ')
	if passWord == 'swordfish':
		break
print 'Access granted.'
