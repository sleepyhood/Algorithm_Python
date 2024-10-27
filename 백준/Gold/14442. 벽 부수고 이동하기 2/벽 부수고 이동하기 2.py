"""
[백준]
14442. 벽 부수고 이동하기 2
https://www.acmicpc.net/problem/14442
"""

import heapq
import sys
import math
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

n, m, k = map(int, input().split())

#sr, sc = map(int, input().split())
#er, ec = map(int, input().split())

sr, sc = 0, 0
er, ec = n-1, m-1

miro = []
visited = [[[0]*(k+1) for _ in range(m)]for _ in range(n)]
# 행, 열, 벽 파괴횟수
# 벽을 파괴할 때마다, 인덱스가 [0]->[1]->[2]->...로 이동

for _ in range(n):
    #miro.append(list(map(int, input().split())))
    miro.append([int(i) for i in input()])

#print(miro) 

visited[sr][sc][0] = 1
q = deque()
q.append([sr, sc, 0])

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

isArrive = False

while q:
    r, c, broken = q.popleft()

    if r==er and c == ec:
        # 끝 지점 도달시, 반복 종료
        print(visited[er][ec][broken])
        isArrive = True
        break

    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]

        if nr < 0 or nr>= n or nc < 0 or nc>=m:
            continue

        if miro[nr][nc] == 0 and not visited[nr][nc][broken] :
            # 벽이 없는 경우 and 현재 벽 파괴상태가 유지되는 경우(방문안된곳)
            q.append([nr, nc, broken])
            visited[nr][nc][broken] = visited[r][c][broken] + 1

        if miro[nr][nc] == 1 and broken + 1 <= k and not visited[nr][nc][broken + 1] :   # 벽을 만나도, 아직 마법을 사용할 수 있다면
            # 벽이 있는 경우 and 벽을 파괴할 수 있다면 and 벽을 파괴할 다음 지역이 방문 안된곳
            q.append([nr, nc, broken + 1])
            # 벽을 파괴한 것으로 간주
            visited[nr][nc][broken + 1] = visited[r][c][broken] + 1
       

# 벽을 파괴안해도, 파괴해도 도달 못할 경우(초기값과 동일)
if not isArrive:
    print(-1)