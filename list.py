a = [66.25, 333, 43, 1,1234.5,333]
print a.count(333), a.count(66.25)

a.insert(2,-1)
a.append(333)
print a

#here insert() takes 2 argument and first agrument
#are index number and second are index value.

print a.index(333)
print a.remove(333)
a.reverse()
print a

a.sort()
print a

a.pop()
print a







stack = [3,4,5]
stack.append(6)
stack.append(7)
print stack
stack.pop()#pop() remove last index value 
print stack
stack.pop()
print stack





#queue means first-in and first-out

from collections import deque

queue = deque (["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
print queue.popleft() # it pops the first index value
print deque
print queue








# fileter (function,sequence)

def f(x):
    return x % 3 == 0 or x % 5 == 0


Filter = filter(f, range(1,11))
# at first give the function name not use parenthesis
# sequence means range() use range
print Filter

def cube(x):
    return x*x*x
Map = map (cube, range(1,20))
print Map


seq = range(8)
print seq

def add(x,y):
    return x + y
Map1 = map(add,seq,seq)
print Map1


#List Comprehensions
squares = []
for x in range(10):
    squares.append(x**2)
print squares

# we can obtain the same result with

squares = [x**2 for x in range(1,100)]
print squares





































