n, m = map(int, input().split())
li = [False] * (m+1)

for i in range(2, m+1):
    if li[i]:
        continue
    for j in range(i**2, m+1, i):
        li[j] = True

for i in range(n,m+1):
    if not li[i] and i > 1:
        print(i)
