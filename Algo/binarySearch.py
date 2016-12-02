def binarySearch(alist, searchValue):
    low = 0
    high = len(alist) - 1
    found = False

    while low <= high and not found:
        midpoint = (low+high) // 2
        if alist[midpoint] == searchValue:
            return True
        else:
            if searchValue > alist[midpoint]:
                low = midpoint + 1
            else:
                high = midpoint - 1
    return found

testSequence = [3,4,5,6,7,8,10]
BS = binarySearch(testSequence, 120)
print BS
