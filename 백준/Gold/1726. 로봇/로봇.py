from collections import deque
import sys
#import math 
#import bisect
"""
[백준]
1726. 로봇
https://www.acmicpc.net/problem/1726
"""

m, n = map(int, input().split())

li = []

for _ in range(m):
    li.append(list(map(int, input().split())))

# 동쪽이 1, 서쪽이 2, 남쪽이 3, 북쪽이 4
# 인덱스로 변환하면 동쪽이 0, 서쪽이 1, 남쪽이 2, 북쪽이 3

sr, sc, sd = (x - 1 for x in map(int, input().split()))
er, ec, ed = (x - 1 for x in map(int, input().split()))

# print(stR)
visited = [[[0] * 4 for j in range(n)] for i in range(m)]

visited[sr][sc][sd] = 1

q = deque()
q.append((sr, sc, sd))

# 주의: 이동은 최소 1칸~최대 3칸까지 한번에 이동이 가능하다.

# 동서남북 순서
dc = [1, -1, 0, 0]
dr = [0, 0, 1, -1]
# print('---------------')

while q:
    r, c, d = q.popleft()
    # print(r, c, d, "\t", visited[r][c][d])

    # 목적지 도달시
    # 시작점은 1이므로 1더 빼주기
    if r == er and c == ec and d == ed:
        print(visited[r][c][d] - 1)
        break


    """명령 1. Go k: k는 1, 2 또는 3일 수 있다. 현재 향하고 있는 방향으로 k칸 만큼 움직인다."""                
    # 이동은 바라보는 방향이 같을 때만 가능
    for p in range(1, 4):
        nr = r + p * dr[d]
        nc = c + p * dc[d]

        if nr < 0 or nc < 0 or nr >= m or nc >= n:
            continue

        # 길인 경우
        if li[nr][nc] == 0:
            if visited[nr][nc][d] == 0:  # 방문 안 한 지점

                visited[nr][nc][d] = visited[r][c][d] + 1
                q.append((nr, nc, d))

        else:
            # 삽질: 최대 3칸까지 간다는 것은, 중간에 벽이 없어야함
            # 길을 건너뛰는 경우도 발생 -> break로 예외처리 하기
            # 0 1 1 0 이 있다면, 이를 무시하는 경우가 존재하므로 조심하기
            break

    """명령 2. Turn dir: dir은 left 또는 right 이며, 각각 왼쪽 또는 오른쪽으로 90° 회전"""
    # 회전을 할 때, 0(동): 2(남), 3(북) / 1(서): 2(남), 3(북) 
    # 회전을 할 때, 2(남): 0(동), 1(서) / 3(북): 0(동), 1(서)

    # 제자리에서 90도 회전도 명령어가 증가한다.

    # ==== 방법 1. if 문으로 구현하기 ====
    # if d == 0 or d == 1:    # 동, 서
    #     if visited[r][c][2] == 0:   # 2(남)으로 회전이 가능한 경우
    #         visited[r][c][2] = visited[r][c][d] + 1
    #         q.append((r, c, 2))
    #     if visited[r][c][3] == 0:   # 3(북)으로 회전이 가능한 경우
    #         visited[r][c][3] = visited[r][c][d] + 1
    #         q.append((r, c, 3))

    # elif d == 2 or d == 3:  # 남, 북
    #     if visited[r][c][0] == 0:   # 0(동)으로 회전이 가능한 경우
    #         visited[r][c][0] = visited[r][c][d] + 1
    #         q.append((r, c, 0))
    #     if visited[r][c][1] == 0:   # 1(서)으로 회전이 가능한 경우
    #         visited[r][c][1] = visited[r][c][d] + 1
    #         q.append((r, c, 1))
            
    # ==== 방법 2. for 문으로 구현하기 ====
    # 동서남북 순서로 회전할 방향을 정의
    turn_left = [3, 2, 1, 0]  # 왼쪽으로 90도 회전
    turn_right = [2, 3, 0, 1]  # 오른쪽으로 90도 회전

    # 왼쪽 회전
    new_d = turn_left[d]
    if not visited[r][c][new_d]:
        visited[r][c][new_d] = visited[r][c][d] + 1
        q.append((r, c, new_d))

    # 오른쪽 회전
    new_d = turn_right[d]
    if not visited[r][c][new_d]:
        visited[r][c][new_d] = visited[r][c][d] + 1
        q.append((r, c, new_d))
 

# for i in visited:
#     print(*i)
