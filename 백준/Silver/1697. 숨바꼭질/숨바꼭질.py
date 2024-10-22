"""
[백준]
1697. 숨바꼭질
https://www.acmicpc.net/problem/1697
"""
import heapq
import sys
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

n, k = map(int, input().split())
# 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동

visited = [0] * 100001
visited[n] = 1

q = deque()
q.append((n, 1))


while q:
    loc, wei = q.popleft()

    if loc == k:
        print(wei-1)
        break
    
    if loc + 1 < 100001 and visited[loc + 1]==0:
        visited[loc + 1] = wei + 1
        q.append((loc+1, wei+1))

    if loc - 1 >= 0 and visited[loc - 1]==0:
        visited[loc - 1] = wei + 1
        q.append((loc-1, wei+1))

    if loc *2 < 100001 and visited[loc*2]==0:
        visited[loc*2] = wei + 1
        q.append((loc*2, wei+1))