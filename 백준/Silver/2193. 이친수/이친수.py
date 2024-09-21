"""
[백준]
2193. 이친수
https://www.acmicpc.net/problem/2193
"""
import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

# 이친수는 0으로 시작하지 않는다.
# 이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.

n = int(input())

dp = [0 for _ in range(91)]


# 1인 경우: 1
dp[1] = 1

# 2인 경우: 10
dp[2] = 1

# 3인 경우: 100, 101
dp[3] = 2

# 4인 경우: 1000, 1001, 1010
dp[4] = 3

for i in range(5, n+1):
    dp[i] = dp[i-1]+dp[i-2]


# 첫째 줄에 N자리 이친수의 개수를 출력한다.
print(f"{dp[n]}\n")