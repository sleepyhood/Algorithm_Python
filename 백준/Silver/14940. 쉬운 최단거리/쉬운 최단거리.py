import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

rows, cols = map(int, (input().rstrip()).split())

_map = list([(input().rstrip()).split() for _ in range(rows)])

startX, startY = 0, 0
_map = [list(map(int, row)) for row in _map]

# 시작 지점 찾기
for i in range(rows):
    for j in range(cols):
        if _map[i][j] == 2:
                #print(f"\n{j} {i}\n")
            startX = j
            startY = i
            break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 여부
visited = [[False for _ in range(cols)]for _ in range(rows)]

que = deque()
que.append((startX, startY))

_map[startY][startX] = 0  #시작점
visited[startY][startX] = True

while que:
    x, y = que.popleft()
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx<0 or nx >= cols or ny <0 or ny>= rows:    # 외벽
            continue
            
        if _map[ny][nx] == 0:    # 내벽
            continue
        elif not visited[ny][nx]:     # 기존 미방문 지역
            _map[ny][nx] = _map[y][x] +1
            visited[ny][nx] = True
            que.append((nx, ny))
            #print(f"nx: {nx} ny: {ny}\n")

for i in range(rows):
    for j in range(cols):   # 갈 수 있으나, 벽에 막힌 곳은  -1로 처리
        if not visited[i][j] and _map[i][j] != 0:
            _map[i][j] = -1
        
            
for i in range(rows):
    for j in range(cols):
        print(f"{_map[i][j]} ")
    print("\n")
