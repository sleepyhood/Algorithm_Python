"""
[백준]
1987. 알파벳
https://www.acmicpc.net/problem/1987
"""
import sys

sys.setrecursionlimit(10000)

def sol(li, r, c, visited, cnt):
    global max_cnt  # 호출마다 증가

    max_cnt = max(max_cnt, cnt)

    #visited[r][c] = val+1
    #val+=1
    
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if nr < 0 or nc < 0 or nr >= len(li) or nc >= len(li[0]):
            continue

        if not(visited & 1<<(ord(li[nr][nc])-ord('A'))) :
            #s.add(li[nr][nc])
            #print(visited | 1<<(ord(li[nr][nc])-ord('A')))
            sol(li, nr, nc, visited | 1<<(ord(li[nr][nc])-ord('A')), cnt+1)
            #s.remove(li[nr][nc])  # 백트래킹을 위해 제거
    

n, m = map(int, input().split())

#visited = [[0 for _ in range(m)]for _ in range(n)]

li = []
s = set()
for _ in range(n):
    li.append([str(i)for i in input().strip()])

s.add(li[0][0])
max_cnt  = 1

# 비트마스크를 통해 알파벳의 방문 여부를 기록
visited =  1 << (ord(li[0][0]) - ord('A'))

sol(li, 0, 0, visited, 1)

#print(*li
#print(visited | (1 << (ord(li[0][1]) - ord('A'))) )
print(max_cnt)