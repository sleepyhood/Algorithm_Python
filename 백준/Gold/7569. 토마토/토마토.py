import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

M, N, H = map(int, (input().rstrip()).split())

# 3차원 배열 초기화
# 열->행->차원
arr_3d = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
visited = deque([])    # 방문예정인 큐도 필요

for i in range(H):
    for j in range(N):
        temp = list(map(int, (input().rstrip()).split()))
        for k in range(M):
            arr_3d[i][j][k] = temp[k]
            if temp[k] == 1: # 토마토가 심어진 위치부터 시작
                visited.append([k, j, i])

# bfs로 너비 확산문제
# 기존 문제들과 달리, 위 아래도 고려해야함-> 방향벡터가 3개
# 방문예정인 큐도 필요

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]



while visited:
    
    x, y, z = visited.popleft()
    
    for i in range(len(dx)):
        nx = x+dx[i]
        ny = y+dy[i]
        nz = z+dz[i]
        
        if nx<0 or nx>=M or ny<0 or ny>=N or nz<0 or nz>=H:    # 외벽
            continue
        if arr_3d[nz][ny][nx] == -1 or arr_3d[nz][ny][nx] == 1:
            continue
        if arr_3d[nz][ny][nx] == 0:
            arr_3d[nz][ny][nx] = arr_3d[z][y][x] + 1
            # 중요: 토마토가 자랄 때마다 지난 날짜를 표기
            visited.append([nx, ny, nz])

days = 0
isFinish = True  
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr_3d[i][j][k] == 0:
                isFinish = False
                break
        days = max(days, max(arr_3d[i][j]))
    #days = max(days, max(arr_3d[i][j]))
    
if isFinish:
    print(f"{days-1}\n")      
else:
    print(f"-1\n")