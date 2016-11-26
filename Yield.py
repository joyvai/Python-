def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k = k + 1
    if k * k == n:
        yield k

mygenarator = factors(100)
print mygenarator


for i in mygenarator:
    print i
