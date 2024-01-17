# 문제의 핵심은, 1의 개수가 아님
# 현재 몇개까지 카운트 했는지가 핵심
import sys
from queue import Queue

input = sys.stdin.readline
print = sys.stdout.write

# M이 x(col), N이 y(row)
N, M = map(int,(input().rstrip()).split())

arr = [[0 for i in range(M)]for j in range(N)]
checkArr = [[0 for i in range(M)]for j in range(N)]

que = Queue()

for i in range(N):
    temp = input().rstrip()
    for j in range(M):
        arr[i][j] = int(temp[j])
        
que.put((0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0,-1, 1]

answer = 0

while not que.empty():    # 비어 있으면 종료

    x, y = que.get()
    isFinal = False
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx<0 or nx>=M or ny<0 or ny>=N:    # 외벽
            continue
        if arr[ny][nx] == 0: # 내벽
            continue
        if arr[ny][nx] == 1: # 길    
            answer +=1
            arr[ny][nx] = arr[y][x] + 1 # 비용을 누적
            que.put((nx, ny)) 
            if nx == M-1 and ny == N-1:    # 목적지 도달
                isFinal = True
                break
                
        if isFinal:
            break
            
print(f"{arr[N-1][M-1]}\n")