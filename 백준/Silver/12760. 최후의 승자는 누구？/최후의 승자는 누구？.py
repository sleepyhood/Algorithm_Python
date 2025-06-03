n, m = map(int, input().split())

li = [0] * n
players = [0] * n

for i in range(n):
    li[i] = list(map(int, input().split()))
    li[i] = sorted(li[i], reverse=True)
    

for j in range(m):
    _max = 0

    # 큰 점수 찾기
    for i in range(n):
        _max = max(_max, li[i][j])

    # 큰 점수있는 유저 점수 증가
    for i in range(n):
        if li[i][j] == _max:
            players[i]+=1


maxPoint = max(players)

for i in range(n):
    if players[i] == maxPoint:
        print(i+1, end=' ')