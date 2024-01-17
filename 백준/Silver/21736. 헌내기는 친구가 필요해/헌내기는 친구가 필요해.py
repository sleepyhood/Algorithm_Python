# 중요: 사람을 만나도 다음 칸으로 이동가능해야함
# 체크용 2차원 배열이 있어야 함
# N: row, M: col
import sys
from queue import Queue

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int,(input().rstrip()).split())

arr = [['O' for i in range(M)]for j in range(N)]
checkArr = [[0 for i in range(M)]for j in range(N)]

doyeonX = 0
doyeonY = 0

for i in range(N):
    temp = input().rstrip()
    for j in range(M):
        arr[i][j] = temp[j]
        
        if temp[j] == 'I':
            doyeonX = j#x가 col
            doyeonY = i#y가 row
            #arr[i][j] = 

que = Queue()
que.put((doyeonY,doyeonX))
checkArr[doyeonY][doyeonX] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0,-1, 1]

answer = 0

while not que.empty():    # 비어 있으면 종료

    y, x = que.get()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if nx<0 or nx>=M or ny<0 or ny>=N:    # 캠퍼스 외벽 or 내벽
            continue
        if arr[ny][nx] == 'X' or checkArr[ny][nx]:
            continue
        if arr[ny][nx] == 'P': # 사람    
            answer +=1
        que.put((ny, nx))
        checkArr[ny][nx] = 1    # 방문 처리


if answer == 0:
    print(f"TT\n")
else:
    print(f"{answer}\n")
    