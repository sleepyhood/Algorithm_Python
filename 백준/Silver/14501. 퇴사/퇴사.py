n = int(input())
T = []  # 상담 기간
P = []  # 상담 수익
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (n + 2)  # n+1일까지 접근 가능해야 하므로 n+2 크기로

for i in range(1, n + 1):
    # 상담을 하지 않는 경우 → 다음 날로 carry
    dp[i] = max(dp[i], dp[i - 1])

    end_day = i + T[i - 1] - 1  # i일부터 시작하면 i+T-1에 끝남

    if end_day <= n:    # 퇴사 전까지만 유효
        dp[end_day] = max(dp[end_day], dp[i - 1] + P[i - 1])

print(max(dp))
