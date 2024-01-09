import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write


N = int(input())
heap = []
heapq.heapify(heap)

result = []

for _ in range(N):
    x = int(input())
    temp = 0
    if x == 0:
        if len(heap)>0: # 가장 작은 값(없으면 0 출력)
            temp = heapq.heappop(heap)
        else:
            temp = 0
            
        result.append(temp)
   
    else:
        heapq.heappush(heap, x)

        
for i in result:
    print(f"{i}\n")
