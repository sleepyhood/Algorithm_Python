t = int(input())

for _ in range(t):
    n = int(input())

    cnt = n // 5
    other = n % 5

    for i in range(cnt):
        print("++++", end=' ')

    for i in range(other):
        print("|", end='')
    print()
    
