# 체크용 2차원 배열이 있어야 함
# N: row, M: col
import sys
from queue import Queue

input = sys.stdin.readline
print = sys.stdout.write
T = int(input().rstrip())

dx = [-1, 1, 0, 0]
dy = [0, 0,-1, 1]

for _ in range(T):
    answer = 0
    # M이 x(col), N이 y(row)
    M, N, K = map(int,(input().rstrip()).split())
    
    arr = [[0 for i in range(M)]for j in range(N)]
    checkArr = [[0 for i in range(M)]for j in range(N)]
    
    que = Queue()

    for i in range(K):
        x, y = map(int,(input().rstrip()).split())
        arr[y][x] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                que.put((j, i))
                answer+=1
                while not que.empty():    # 비어 있으면 종료
                    x, y = que.get()

                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]

                        if nx<0 or nx>=M or ny<0 or ny>=N:    # 외벽
                            continue
                        if arr[ny][nx] == 0: # 내벽
                            continue
                        if arr[ny][nx] == 1: # 배추    
                            que.put((nx, ny))
                            arr[ny][nx] = 0

    print(f"{answer}\n")