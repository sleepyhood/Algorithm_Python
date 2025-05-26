n, h = map(int, input().split())

li = [0]*n
cave = [[] for i in range(2)]   # 0번은 석순, 1번은 종유석

for i in range(n):
    li[i] = int(input())
    cave[i%2].append(li[i])


# 누적합 
# 석순(L->R)과 종유석(R->L)
# 시작 지점을 1, 끝나는 다음칸을 0 넣기


up = [0] * (h+2)
down = [0] * (h+2)

for e in cave[0]:   # 석순
    down[1] += 1
    down[e+1] -= 1

for e in cave[1]:   # 종유석
    up[h] += 1
    up[h-e] -= 1

for i in range(1, h+1):
    down[i] += down[i-1]

for i in range(h, 0, -1):
    up[i-1] += up[i]

result = [0]*(h+2)

for i in range(h+2):
    result[i] = up[i]+down[i]

# 주의: 양끝은 계산범위에 포함되지 않기        
MIN = min(result[1:h+1])

print(MIN, result[1:h+1].count(MIN))