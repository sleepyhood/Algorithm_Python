n = int(input())
loc = list(map(int, input().split()))
time = list(map(int, input().split()))

# 중간에 내가 더 시간을 많이 소모할 경우, 다시 돌아올 때 회수하면됌.

# 왼->오 갈 때는 현재 시간보다 짧은 것만 회수하기
total = 0

# 거리 배열
dist = [loc[0]]

for i in range(n-1):
    dist.append(loc[i+1]-loc[i])

# 1. 왼쪽->오른쪽
for i in range(n):
    total+=dist[i]

    if time[i] > total: # 시간 많이 먹는 곳은 나중에 다시 오기로
        continue
    #time[i] = -1

# 2. 오른쪽 -> 왼쪽
for i in range(n-1, -1, -1):
    if time[i] > total:
        total+= (time[i]-total)

    total+=dist[i]

print(total)

