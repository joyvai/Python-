j = 1
def swap(aList):
    #[3,2,1]
    for i in (aList):
        temp = aList[i] # temp = aList[0]=3
        aList[i] =aList[i+1] #aList[0] =aList[1]
        aList[i+1] = temp
    return aList
print (swap([3,2,1]))
    
