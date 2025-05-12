n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()


# 왕복 거리가 있으므로, 상대적으로 가까운곳부터 방문하는것이 최선
# 가장 먼곳에 갈 때는 다시 돌아올 필요가 없다.
minus = []
plus = []

total = 0

for e in li:
    if e > 0:
        plus.append(e)
    else:
        minus.append(e)

plus.reverse()  # 양수도 큰 곳부터 방문

for i in range(0, len(plus), m):
    total+=(plus[i]*2)

for i in range(0, len(minus), m):
    total+=abs(minus[i])*2



dist = [abs(i) for i in li]

total-= max(dist)
print(total)
