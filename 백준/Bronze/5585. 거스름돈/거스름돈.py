n = int(input())
n = 1000-n

coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for e in coins:
    cnt += n // e
    n%=e
print(cnt)    