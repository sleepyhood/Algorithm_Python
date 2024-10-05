"""
[백준]
16928. 뱀과 사다리 게임
https://www.acmicpc.net/problem/16928
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

board = [0 for _ in range(101)]
visited = [-1 for _ in range(101)]

for _ in range(n):
    x, y =  map(int, input().split())
    board[x] = y

for _ in range(m):
    u, v =  map(int, input().split())
    board[u] = v

q = deque()

# 시작점
visited[1] = 0
q.append(1)


while q:
    loc = q.popleft()
    
    if loc == 100:
        print(visited[loc])
        break

    for i in range(1, 7):        # 주사위 횟수 만큼 반복

        if loc + i > 100:
            continue

        nLoc = loc+i   # 보드에서 다음 위치

        if board[nLoc]!=0:      #연결된 사다리 또는 뱀
            nLoc = board[nLoc]


        if visited[nLoc] == -1:   
            visited[nLoc] = visited[loc]+1
            #print(loc, nLoc)
            q.append(nLoc)