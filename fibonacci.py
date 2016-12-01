def fib():
    Lfib = [0,1]
    takeInput=int(raw_input("How many fibonacci numbers do you want:  "))
    for i in range(takeInput - 2):
        Lfib.append(Lfib[-2]+Lfib[-1])
    return Lfib
Fib = fib()
print Fib
