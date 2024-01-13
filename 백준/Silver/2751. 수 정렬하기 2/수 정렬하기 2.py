import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
heap = []

for i in range(n):
    value = int(input().rstrip())
    heapq.heappush(heap, value)
#temp.append(value)
#
#temp.sort()
while heap:
    print(f"{heapq.heappop(heap)}\n")