"""
[백준]
11725. 트리의 부모 찾기
https://www.acmicpc.net/problem/11725
"""

import heapq
import sys
import math
from collections import deque

sys.setrecursionlimit(100000)  # 재귀 한도를 높여줍니다.

# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
INF = float(1e9)

#input = sys.stdin.readline
#print = sys.stdout.write
#n, k = map(int, input().split())
n = int(input())
parents = [0 for i in range(n+1)]
graph = [[] for _ in range(n+1)]
parents[1] = 0  # 루트 1번은 부모가 없으므로 0

# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 
# 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

def dfs(node, graph, parents):
   
    for e in graph[node]:
        if parents[e]==0:
            parents[e] = node
            dfs(e, graph, parents)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)

#print(graph)
for i in range(1, n+1):
    dfs(i, graph, parents)


# 2번 노드부터 부모 출력
for i in range(2, n+1):
    print(parents[i])