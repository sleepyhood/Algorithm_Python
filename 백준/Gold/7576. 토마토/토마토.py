import sys
from collections import deque    # dq를 써야만 시간초과 없음

# 7569번은 차원이 하나더 늘어나는 심화판
input = sys.stdin.readline
print = sys.stdout.write

# M이 col, N이 row
M, N = map(int, (input().rstrip()).split())

# 2차원 배열 초기화
# 열->행->차원
arr_2d = [[0 for _ in range(M)] for _ in range(N)]
visited = deque([])    # 방문예정인 큐도 필요

for j in range(N):
    temp = list(map(int, (input().rstrip()).split()))
    for k in range(M):
        arr_2d[j][k] = temp[k]
        if temp[k] == 1: # 토마토가 심어진 위치부터 시작
            visited.append([k, j])
            

# bfs로 너비 확산문제
# 방향벡터가 2개
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
days = 0

while visited:
    
    x, y = visited.popleft()
    
    for i in range(len(dx)):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=M or ny<0 or ny>=N:    # 외벽
            continue
        if arr_2d[ny][nx] == -1 or arr_2d[ny][nx] == 1:
            continue
        if arr_2d[ny][nx] == 0:
            arr_2d[ny][nx] = arr_2d[y][x] + 1
            # 중요: 토마토가 자랄 때마다 지난 날짜를 표기
            visited.append([nx, ny])

isFinish = True            
for i in range(N):
    for j in range(M):
        if arr_2d[i][j] == 0:
            isFinish = False
            break
    days = max(days, max(arr_2d[i]))
            
if isFinish:
    print(f"{days-1}\n")      
else:
    print(f"-1\n")