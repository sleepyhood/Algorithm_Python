"""
[백준]
9461. 파도반 수열
https://www.acmicpc.net/problem/9461
"""

import heapq
import sys
import math
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write


# 입력
t = int(input())

#n, m, v = map(int, input().split())
dp = [0 for _ in range(101)]
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
dp[1:4] = [1,1,1]
# 현재 변의 길이 = 2번째 이전 변 + 3번때 이전 변

for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(t):
    n = int(input())
    print(dp[n])