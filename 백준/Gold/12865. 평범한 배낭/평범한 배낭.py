n, k = map(int, input().split())
weights = [0] * (n+1)
values = [0] * (n+1)

for i in range(1, n+1):
    weights[i], values[i] = map(int, input().split())

dp = [ [0] * (k+1) for i in range(n+1)]

# DP의 행은 각각 물건
# DP의 열은 현재 무게, 최대 가방의 무게까지만 허용

for i in range(1, n+1):
    for j in range(1, k+1):
        w = weights[i]
        v = values[i]
        # 1. 현재 가방에 못 넣는 경우, 이전에 넣은 무게만 반영
        if w > j:
            dp[i][j] = dp[i-1][j]
        
        # 2. 기존에 넣은 무게를 빼고 새로 넣는 경우
        # 이 때, 새로 넣을만큼 무게를 제외
        # 현재 i번째 물건을 담는 경우 vs 현재 i번째 물건을 안 담는 경우 
        else:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])

print(dp[n][k])

