"""
[백준]
11727. 2×n 타일링 2
https://www.acmicpc.net/problem/11727
"""

import heapq
import sys
import math
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

#n, m, d = map(int, input().split())

# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 
# 방법의 수를 구하는 프로그램을 작성하시오.

n = int(input())

dp = [0] * (1001)

# 2*1 채우기
dp[1] = 1

# 2*2 채우기
# 일자 2개와 정사각형 1개
dp[2] = 2 + 1

# 2*3 채우기
dp[3] = dp[2] + dp[1] + dp[1]

for i in range(4, n+1):
    dp[i] = (dp[i-1] + dp[i-2]+ dp[i-2]) % 10007

print(dp[n])