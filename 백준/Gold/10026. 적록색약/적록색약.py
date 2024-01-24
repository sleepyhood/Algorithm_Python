import sys
from collections import deque

# 2667 단지번호와 비슷한 문제
# 시작지점이 따로 있는게 아니므로, 탐색 지점에서 시작
# 중요: 2개의 방문여부를 사용하지 않고, 정상인것부터 하고 색을 2가지로 만듦(R, G 중 R로 통합하는식)

def bfs(findColor, x, y):
    
    color.append((x,y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while color:
        x, y = color.popleft()
        visited1[y][x] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx >= N or ny < 0 or ny >=N:
                continue
            if visited1[ny][nx] == False and picMap[ny][nx] == findColor:
                # 적록 색약인 경우에는 R또는 G를 하나의 케이스로 처리해야한다.
                color.append((nx,ny))
                visited1[ny][nx] = True

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

#picMap = [['0' for _ in range(N)] for _ in range(N)]

color = deque()


"""
for i in range(N):
    temp = input().rstrip()
    for j in range(N):
        picMap[i][j] = temp[j]
"""
picMap = [list(input().strip()) for _ in range(N)]

res1 = 0
res2 = 0  

# 2개의 방문여부 2차원 리스트 생성
visited1 = [[False for _ in range(N)] for _ in range(N)]    # 정상
#visited2 = [[0 for _ in range(N)] for _ in range(N)]    # 적록색약

for i in range(N):
    for j in range(N):
        if visited1[i][j]==False:  # 정상
            bfs(picMap[i][j], j, i)
            res1 +=1
            
for i in range(N):
    for j in range(N):
        if picMap[i][j]=='G':  # 초록을 R로(적록색약은 같게 판단)
            picMap[i][j]='R'

visited1 = [[False for _ in range(N)] for _ in range(N)]    # 적록색약 버전
            
for i in range(N):
    for j in range(N):          
        if visited1[i][j] == False: # 적록색약  
            bfs(picMap[i][j], j, i) 
            res2 += 1

print(f"{res1} {res2}\n")    