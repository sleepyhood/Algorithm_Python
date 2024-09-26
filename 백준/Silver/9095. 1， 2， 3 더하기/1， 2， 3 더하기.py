"""
[백준] 1, 2, 3 더하기
https://www.acmicpc.net/problem/9095
"""

t = int(input())

dp = [0 for _ in range(11)]

# 1: 1
dp[1] = 1

# 2: 1만들기*2, 2
dp[2] = 2

# 3: 1+1+1, 1+2, 2+1, 3
dp[3] = 4

# 4: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1
dp[4] = dp[3] + dp[2] + dp[1]

# dp[i] = dp[i-k] + dp[k]
# 이 때 해당 숫자(i)를 만드는 경우는 반복문을 통해서 경우의 수를 계산하기

for i in range(5, 11):
    dp[i] += dp[i-3] + dp[i-2] + dp[i-1] 

for i in range(t):
    n = int(input())
    print(dp[n])