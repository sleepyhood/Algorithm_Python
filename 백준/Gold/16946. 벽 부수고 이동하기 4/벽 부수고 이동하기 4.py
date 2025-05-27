#import sys
from collections import deque
#sys.setrecursionlimit(100000)

n, m = map(int, input().split())

li = [0]*n
visit = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
     tmp = list(input())
     li[i] = [int(e) for e in tmp]

# 1. 0으로 채워진 곳들 찾기(미리 계산하기)     

mr = [-1,1,0,0]
mc = [0,0,-1,1]

# dfs로는 재귀함수가 시간초과 및 재귀 에러
# def dfs(r, c, num):
#     visit[r][c] = num
#     global size
#     size +=1
#     for i in range(4):
#         nr = r + mr[i]
#         nc = c + mc[i]

#         if nr < 0 or nc < 0 or nr >= n or nc>=m:
#             continue
#         if visit[nr][nc]:
#             continue
#         if li[nr][nc] == 1:
#             continue

#         dfs(nr, nc, num)

def bfs(r, c, num):
    
    size = 1
    q = deque()
    q.append([r, c])
    
    while len(q):
        r, c = q.popleft()
        visit[r][c] = num

        for i in range(4):
            nr = r + mr[i]
            nc = c + mc[i]

            if nr < 0 or nc < 0 or nr >= n or nc>=m:
                continue
            if visit[nr][nc]:
                continue
            if li[nr][nc] == 1:
                continue
            visit[nr][nc] = num
            q.append([nr, nc])
            size+=1

    return size

##############################################

num = 1     # 0 구역의 번호
size = 0    # 0 구역의 크기 
dic = {}    # 0 구역 번호별 크기

for i in range(n):
    for j in range(m):
        if li[i][j] == 0 and not visit[i][j]:
            #size = 0
            dic[num] = bfs(i, j, num)
            num+=1


# 2. 벽인 곳들 뚫는다고 가정하고 시뮬레이션 돌리기
res = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):         
        if li[i][j] == 1 and not visit[i][j]:
            #visit[i][j] = -1
            tmp = 0
            # 4곳을 돌리기
            # 이미 계산한 구역의 값 이용하기
            s = set()   # 중복 계산 막기
            for k in range(4):
                nr = i + mr[k]
                nc = j + mc[k]

                if nr < 0 or nc < 0 or nr >= n or nc>=m:
                    continue
                if visit[nr][nc] == 0:  # 벽은 방문 처리 안하고, 아예 안 가기
                    continue
                if visit[nr][nc] in s:  # 이미 본 구역이라면, 넘기기
                    continue
                tmp += dic[visit[nr][nc]]
                s.add(visit[nr][nc])
            res[i][j] = tmp+1

# 중요: 벽인 곳은 이동할 수 있는 칸의 개수를 10으로 나눈 나머지를 출력
for e in res:
    #e = ''.join(e)
    e = ''.join([str(x%10) for x in e])
    print(e)

#print(dic)