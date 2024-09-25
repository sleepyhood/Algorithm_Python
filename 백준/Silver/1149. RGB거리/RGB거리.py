"""
[백준]
1149. RGB거리
https://www.acmicpc.net/problem/1149
"""
import heapq
import sys
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

n = int(input())

li = []
for i in range(n):
    li.append(list(map(int, input().split())))


dp = [[0 for _ in range(3) ] for _ in range(n)]

dp[0][0] = li[0][0]     # 첫번째 R선택
dp[0][1] = li[0][1]     # 첫번째 G선택
dp[0][2] = li[0][2]     # 첫번째 B선택

# 핵심: 현재 색상의 값과, 이전행에서 (현재색상 제외)한 것중 최소값을 가져오기
# 최종적으로 어떤 색상이 효율적인지는 마지막 행에서 판별

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + li[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + li[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + li[i][2]

# 마지막행 기준, RGB 최소값 찾기
print(min(dp[n-1]))