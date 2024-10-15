"""
[백준]
1916. 최소비용 구하기
https://www.acmicpc.net/problem/1916
"""

import heapq
import sys
import math
from collections import deque

# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('inf')
INF = 99999999
#input = sys.stdin.readline
#print = sys.stdout.write

#n, m = map(int, input().split())
n = int(input())
m = int(input())

# 인접 리스트 초기화
li = [[]for _ in range(n+1)]


# 인접 리스트 입력
for _ in range(m):
    a,b, w= map(int, input().split())
    li[a].append((b, w))    # 목적지, 가중치 순서

st, ed = map(int, input().split())    # 시작, 끝 번호

# 각 정점별 연결거리 (초기값은 무한히 큰 값)
nodes = [INF for _ in range(n+1)]
nodes[st] = 0
# 시작지점은 자기자신이므로 0

# 최소 힙
pq = []
# (거리, 정점) 형태로 추가
# 주의: 거리가 짧은것을 우선적으로 두어야 하기 때문에
heapq.heappush(pq, (0, st)) # 시작점

# =========자료구조 준비 완료===========

# 다익스트라 시작
while pq:
    weight, dest = heapq.heappop(pq)
    
    # 새로 본 가중치가 더 큼(이미 방문이 된 곳)
    if weight > nodes[dest]:
        continue


    # 현재 위치에서 탐색
    for nextDest, nextWeight in li[dest]:
        # nextDest이 목적지, nextWeight은 가중치

        newWeight = weight + nextWeight

        if newWeight < nodes[nextDest]:
        # 더 짧은 위치를 찾았다면
            nodes[nextDest] = newWeight
            heapq.heappush(pq, (newWeight, nextDest))

print(nodes[ed])