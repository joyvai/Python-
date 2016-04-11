"""
When you call sayHello() , the argument is assigned to the name parameter. Parameters are just
ordinary local variables. Like all local variables, the values in parameters will be forgotten when
the function call returns.

"""


def sayhello(name):
	print 'Hello,' + name + '. Your name has ' + str(len(name)) +  ' letters.'

sayhello(raw_input("Give me your name: "))
spam = 'carol'
sayhello(spam)
