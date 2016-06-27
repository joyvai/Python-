movieName = []

while True:
	print 'Please Enter your favorite Movie ' + str(len(movieName)+1)
	print 'If you want to exit , just write "stop" '
	name = raw_input ()
	if name.lower() == 'stop':
		break
	movieName = movieName + [name]
print 'Here is the list of movie name => '
for name in movieName:
	print ' ' + name
