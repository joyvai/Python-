def Count():
	count = 0
	zork = ['joy','joya','jan','jane']
	for thing in zork:
		count += 1
		print count,thing.upper()
	print 'total count:%d ' %count
Count()
