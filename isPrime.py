# def isPrime(n):
#     if n <= 1:
#         return 0
#     i = 2
#     while i < n:
#         if n % i == 0:
#             return 0
#         i = i + 1
#     return "prime"
#
# print isPrime(int (raw_input()))

def isPrime( n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True

print isPrime(int (raw_input()))
