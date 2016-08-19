def insertionSort(alist):
	for index in range(1,len(alist)):
		currentValue = alist[index]
		position = index

		while position > 0 and alist[position-1] > currentValue:
			alist[position] = alist [position-1]
			position = position -1
		alist[position] = currentValue

alist = [5,2,4,6,1,3]
insertionSort(alist)
print alist
