"""
[백준]
2096. 내려가기
https://www.acmicpc.net/problem/2096
"""

import sys
import heapq
#input = sys.stdin.readline
#print = sys.stdout.write

n = int(input().strip())


# 메모리때문에 입력받자마자 DP 계산
dpMax = []
dpMin = []

for i in range(n):
    li = list(map(int, input().split()))
    if i == 0:
        # 얉은 복사 문제;;;
        dpMax = li[:]
        dpMin = li[:]

    else:
        a,b,c = li
        # 가장 왼쪽에 더할 값, 가운데에 더해질 값, 가장 오른쪽에 더할 값
        maxRow = [a + max(dpMax[0], dpMax[1]), b + max(dpMax), c + max(dpMax[1], dpMax[2])]
        minRow = [a + min(dpMin[0], dpMin[1]), b + min(dpMin), c + min(dpMin[1], dpMin[2])]

        dpMax, dpMin = maxRow, minRow

    

print(max(dpMax), min(dpMin))