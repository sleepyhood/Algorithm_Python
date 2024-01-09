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
            temp = heapq.heappop(heap)[1]
        else:
            temp = 0
            
        result.append(temp)
   
    else:           # -는 최대 힙을 기준으로 함
        heapq.heappush(heap, (-x, x))

        
for i in result:
    print(f"{i}\n")
