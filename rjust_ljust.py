# Justifying Text with rjust(),ljust(), and center()

print 'Hello'.rjust(10)
# 'Hello'.rjust(10) says that we want to right-justify 'Hello' in a 
# string of total length 10.'Hello' is five characters,
# so five spaces will be added to its left, giving us a
# string of 10 characters with 'Hello' justified right.

print 'Hello'.rjust(20)
print 'Hello World'.rjust(20)
print 'Hello'.ljust(10)

print 'Hello'.rjust(20,'*')
print 'Hello'.ljust(20,'-')

print 'Hello'.center(20)
print 'Hello'.center(20,'=')
