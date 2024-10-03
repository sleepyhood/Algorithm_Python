"""
[백준]
1072. 게임
https://www.acmicpc.net/problem/1072
"""

import heapq
import sys
import math
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

"""
게임 횟수 : X
이긴 게임 : Y (Z%)
Z는 형택이의 승률이고, 소수점은 버린다. 예를 들어, X=53, Y=47이라면, Z=88이다.
X와 Y가 주어졌을 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.
"""

# 입력    
#t = int(input())
x, y = map(int, input().split())

z = (y * 100) // x  # 기존 승률 정수 계산 (소수점 없이)
#print(z)
cnt = 0

#print(f"초기: {z}")

if z>=99:
    cnt = -1    # 이미 승률이 1
else:
    l, r = 0, 1000000000

    while l<=r:
        mid = (l+r)//2  
        nx = x+mid  # 새로운 시도 횟수
        ny = y+mid  # 새로운 승리 횟수
        nz = (ny * 100) // nx    # 새로운 승률
        #print(f"nz: {nz}")
        if nz > z:      # 승률이 기존보다 오를 경우(답을 찾은 경우와 일치)
            cnt = mid   
            r = mid - 1 # 구간 좁히기(오른쪽을 줄이기)
        else:
            l = mid+1   # 구간 좁히기(왼쪽을 줄이기)

print(cnt)