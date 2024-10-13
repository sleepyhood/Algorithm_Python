"""
[백준]
1753. 최단경로
https://www.acmicpc.net/problem/1753
"""

import heapq
import sys
import math
from collections import deque

# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('inf')
INF = 999999
#input = sys.stdin.readline
#print = sys.stdout.write

n, e = map(int, input().split())
k = int(input())    # 시작 번호

# 인접 리스트 초기화
# 목적지, 가중치 순서
li = [[] for i in range(n+1)]

# 인접 리스트 입력
for _ in range(e):
    u, v, w = map(int, input().split())
    li[u].append((v, w))

# 각 정점별 연결거리 (초기값은 무한히 큰 값)
nodes = [INF for _ in range(n+1)]
nodes[k] = 0    # 시작지점은 자기자신이므로 0

# 최소 힙
pq = []
heapq.heappush(pq, (nodes[k], k))   # (거리, 정점) 형태로 추가

# =========자료구조 준비 완료===========

# 다익스트라 시작
while pq:
    weight, dest = heapq.heappop(pq)

    # 새로 본 가중치가 더 큼(이미 방문이 된 곳)
    if weight > nodes[dest]:
        continue

    # 현재 위치에서 탐색
    for nextDest, nextWeight in li[dest]:  # 1번 정점부터 연결된 지역 시작
        # nextDest이 다음 지역, nextWeight은 가는데 필요한 비용
        newWeight = weight+nextWeight

        # 더 짧은 위치를 찾았다면
        if newWeight < nodes[nextDest]:
            nodes[nextDest] = newWeight
            heapq.heappush(pq, [newWeight, nextDest])

for i in range(1, n+1):
    if nodes[i]==INF:
        print("INF")
    else:
        print(nodes[i])