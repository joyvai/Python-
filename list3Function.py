
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
