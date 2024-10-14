"""
[백준]
11404. 플로이드
https://www.acmicpc.net/problem/11404
"""

import heapq
import sys
import math
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
INF = float(1e9)

#input = sys.stdin.readline
#print = sys.stdout.write
n = int(input())
m = int(input())

# 도시 연결 그래프
# 초기값은 크게, 점점 최소값으로
graph = [[INF for j in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0 # 자기 자신은 가중치 없음

for _ in range(m):
    a, b, k = map(int, input().split())
    # a→b 노선이 하나만 있지는 않음, 최소 비용만 기억하기
    graph[a][b] = min(graph[a][b] , k)


for k in range(1, n+1): # 1~n번을 경유하는 경우
    for i in range(1,n+1):  # 출발지
        for j in range(1, n+1): # 목적지
            # 경유(K)하는게 더 최소값이라면 갱신
            if (graph[i][k] + graph[k][j]) < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]


for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:  # 여전히 갈 수 없다면, 0으로 출력하기
            graph[i][j] = 0
        print(graph[i][j], end=" ")
    print()

