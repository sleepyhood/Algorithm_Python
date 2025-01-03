n = int(input())
a, b = map(int, input().split())

total = a//2 + b

if total <= n:
    print(total)
else:
    print(n)