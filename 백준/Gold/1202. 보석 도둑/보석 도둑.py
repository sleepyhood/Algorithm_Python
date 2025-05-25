import heapq

n, k = map(int,input().split())

gems= []
bags = []
#maxDay = 0

for _ in range(n):
    m, v= map(int, input().split())
    gems.append([m, v])

    
for _ in range(k):
    c = int(input())
    bags.append(c)

# 보석 무게와 가방 오름차순
gems.sort()
bags.sort()

#print(bags)

max_value_heap  = []
idx = 0
result = 0

for bag in bags:

    # 가방에 넣을 수 있는 보석들은 다 모아보기
    # 만약 이번에 못 넣어도, 그 다음으로 넣은 보석들 찾기
    while idx < len(gems) and gems[idx][0] <= bag:
        heapq.heappush(max_value_heap, -gems[idx][1])   # 최대값 힙, 가벼우면서 최대가치가 들어감
        # 맨 앞에 최대가치
        idx+=1

    # 못 넣은 경우도 있을 수 있다.
    # 힙에 항상 있다는 보장은 없다.
    if len(max_value_heap) > 0:
        result+=(-heapq.heappop(max_value_heap))    
                
print(result)
