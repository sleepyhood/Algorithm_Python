n = int(input())

for i in range(n, 10**9+1):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if not isPrime: 
        print(i)
        break
            