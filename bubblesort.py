def shortBubbleSort (alist):
    exchanges = True # it's a flag or boolean test
    passnum = len(alist) -1 # passnum = 6 - 1 = 5
    while passnum > 0 and exchanges: # 5 > 0 and exchanges = True
        exchanges = False 
        for i in range(passnum):
            if alist[i] > alist[i+1]:#if this statement is true
                exchanges=True # then line 8 works
                temp = alist[i] # temp is a temporary single variable 
                alist[i]=alist[i+1]
                alist[i+1] = temp
            # end if
        # end for
    # end while
        passnum = passnum -1 # decrease the value
alist = [90,80,70,60,50,40]
shortBubbleSort(alist)
print alist
