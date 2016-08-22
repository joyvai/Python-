import time
def calcProd():
	# Calculate the product of the first 100,000 numbers
	product = 1
	# This loop start 1 and end 99,999
	# return their product.
	for i in range(1, 100000):
		product = product * i
	return product
startTime = time.time()
print "Start Time: %d" %startTime
prod = calcProd()
endTime = time.time()
print "End Time: %d " %endTime
# printing the length of product returned by calcProd()
print 'The result is %s digits long.' %(len(str(prod)))
print 'Took %s seconds to calculate.' % (endTime - startTime)
