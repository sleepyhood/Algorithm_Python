a, b = map(int, input().split())

res = a - a*(b/100)

if res >= 100:
    print(0)
else:
    print(1)