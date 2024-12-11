"""
[백준]
2891. 카약과 강풍
https://www.acmicpc.net/problem/2891
"""

from collections import deque
import heapq
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('inf')
INF = 99999999
#input = sys.stdin.readline
#print = sys.stdout.write

n, s, r = map(int, input().split())

li = [1 for i in range(n+1)]
dm = list(map(int, input().split()))
rr = list(map(int, input().split()))

for e in dm:
    li[e]-=1

for e in rr:
    li[e]+=1

for i in range(1, n):
    if li[i] == 0 and li[i+1] >= 2:
        li[i] +=1
        li[i+1] -=1
    elif li[i] >= 2 and li[i+1] == 0:
        li[i] -=1
        li[i+1] +=1

#print(li)
print(li.count(0))
"""
5 3 1
5
4
"""