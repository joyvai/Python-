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
