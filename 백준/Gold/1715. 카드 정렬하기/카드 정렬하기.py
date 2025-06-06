import heapq


n = int(input())

q = []

for i in range(n):
    k = int(input())
    heapq.heappush(q, k)

total = 0

while len(q) >= 2:
    a = heapq.heappop(q)
    b = heapq.heappop(q)

    tmp = a+b
    total+= tmp

    heapq.heappush(q, tmp)
print(total)


