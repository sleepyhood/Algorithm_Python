r, c = map(int, input().split())
l = [input() for _ in range(r)]  # 입력받기

dp = [[0 for _ in range(c)] for _ in range(r)]
dp[r-1][c-1] = 1  # 도착점에서 출발하는 경우 1


# 역순 탐색: 도착점부터 출발점 방향으로 진행
for u in range(c-1, -1, -1):
    for v in range(r-1, -1, -1):
        for i in range(v+1, r):  # 아래쪽으로만 이동 가능
            for j in range(u+1, c):  # 오른쪽으로만 이동 가능
                if l[v][u] != l[i][j]:  # 색깔이 다르면 점프 가능
                    dp[v][u] += dp[i][j]  # 가능한 경로 개수 추가

print(dp[0][0])  # (0,0)에서 출발하는 경우의 수 출력