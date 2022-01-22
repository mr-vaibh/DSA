def fibbonaci(n):
    if n == 0 or n == 1:
        return n
    return fibbonaci(n-1) + fibbonaci(n-2)

for i in range(20):
    print(fibbonaci(i), end=" ")