"""
[백준]
14923. 미로 탈출
https://www.acmicpc.net/problem/14923
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

sr, sc = map(int, input().split())
er, ec = map(int, input().split())

sr, sc = sr-1, sc -1
er, ec = er-1, ec -1

miro = []
visited = [[[0]*2 for _ in range(m)]for _ in range(n)]
#broken = [[[0]*2 for _ in range(m)]for _ in range(n)]   # 벽 파괴 여부

for _ in range(n):
    miro.append(list(map(int, input().split())))


#print(miro) 

visited[sr][sc][0] = 1
q = deque()
q.append([sr, sc, 0])

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while q:
    r, c, used = q.popleft()

    if r==er and c == ec:
        print(visited[er][ec][used]-1)
        break

    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]

        if nr < 0 or nr>= n or nc < 0 or nc>=m:
            continue

        if miro[nr][nc] == 0 and not visited[nr][nc][used] :
            # 벽이 없는 경우
            q.append([nr, nc, used])
            visited[nr][nc][used] = visited[r][c][used] + 1

        if miro[nr][nc] == 1 and used == 0 and not visited[nr][nc][1] :   # 벽을 만나도, 아직 마법을 사용할 수 있다면
            q.append([nr, nc, 1])
            visited[nr][nc][1] = visited[r][c][used] + 1
       

   

# for e in visited:
#    print(e)
   #print()

if visited[er][ec][0] ==0 and visited[er][ec][1] ==0 :
    print(-1)