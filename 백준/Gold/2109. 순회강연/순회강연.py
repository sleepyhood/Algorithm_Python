import heapq

n = int(input())

arr = []
maxDay = 0

for _ in range(n):
    p, d= list(map(int, input().split()))
    arr.append([d, p])
    maxDay = max(maxDay, d)
    # heapq.heappush(gems, [w,v,v/w])
    
# 마감일 기준으로 오름차순 정렬
arr.sort()

days = []

s = 0

for d, p in arr:
    #print(days[d])
    heapq.heappush(days, p)
    # d일 이내에 가능한 강연 수는 d개뿐
    if len(days) > d:
        heapq.heappop(days)  # 가장 싼 강연 빼버림
        # 자동으로 가장 앞에 싼 강의가 들어감
    #print(days)

print(sum(days))
