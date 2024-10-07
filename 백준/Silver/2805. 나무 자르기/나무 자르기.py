"""
[백준]
2805. 나무 자르기
https://www.acmicpc.net/problem/2805
"""

import heapq
import sys
import math
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

n, m = map(int, input().split())

li = list(map(int, input().split()))

# 상근이는 집에 필요한 나무를 항상 가져갈 수 있다.
l, r = 0, max(li)+1
ans = 0     # 나무의 최대 높이

# 벌목 높이가 높다-> 원하는 만큼의 목재를 못 가져갈 수 있다.
# 벌목 높이가 낮다-> 목재는 많아지지만, 나무를 최대한 길게 남을 수 있는지는 불확실

while l<=r:
    mid = (l+r) // 2

    result = sum(map(lambda e: 0 if e <= mid else e - mid, li))
    # 높이 mid로 벌목했을 때 남은 나무의 양
    #print(f"mid: {mid}\tresult:{result}")
    if result < m:  # 남은 나무가 목표보다 적다면
        # 벌목 높이를 더 낮춰야함
        r = mid - 1
    else:
        if result>=m:   # 원하는 목재만큼을 확보했다면
            ans = max(mid, ans) # 그 중 최대 높이만 기억
        # 벌목 높이 올리기
        l = mid + 1

print(ans)