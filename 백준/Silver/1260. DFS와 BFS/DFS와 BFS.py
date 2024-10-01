"""
[백준]
1260. DFS와 BFS
https://www.acmicpc.net/problem/1260
"""

import heapq
import sys
import math
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write



def dfs(node, n, li, visited):

    visited[node] = 1
    print(node, end=' ')

    for i in range(1, n+1):
        #print(i, ":", li[node][i])
        if li[node][i] == 1 and visited[i]==0:
            dfs(i, n, li, visited)
    #return

def bfs(n, li, visited, q):

    while len(q):
        node = q.popleft()
        visited[node] = 1
        print(node, end= ' ')

        for i in range(1, n+1):
            if li[node][i] == 1 and visited[i]==0:
                visited[i] = 1
                q.append(i)

n, m, v = map(int, input().split())

li = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    li[a][b] = 1
    li[b][a] = 1

visited = [0 for _ in range(n+1)]
# DFS
dfs(v, n, li, visited)

print()

visited = [0 for _ in range(n+1)]
q = deque()
q.append(v)
# BFS
bfs(n, li, visited, q)