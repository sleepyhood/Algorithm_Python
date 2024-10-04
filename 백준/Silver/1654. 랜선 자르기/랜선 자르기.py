"""
[백준]
1654. 랜선 자르기
https://www.acmicpc.net/problem/1654
"""

import heapq
import sys
import math
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write
n, k = map(int, input().split())

li = []
_max = 0
for _ in range(n):
    li.append(int(input()))
    _max = max(li)    
    
#print(_max)

l, r = 1, _max+1
ans = 0
while l<=r:
    mid = (l+r) // 2

    _sum = sum([(i // mid )for i in li])    # 막대의 개수
    #print(_sum)
    if _sum < k:    # 랜선 개수가 아직 k개에 못 미칠 경우, 더 잘게 쪼개야함
        r = mid -1
    else:   
        ans = max(ans, mid)
        l = mid + 1

print(ans)       