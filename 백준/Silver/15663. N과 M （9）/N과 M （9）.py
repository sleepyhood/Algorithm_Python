"""
[백준]
15663. N과 M (9)
https://www.acmicpc.net/problem/15663
"""

from collections import deque

# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('inf')
INF = 99999999
#input = sys.stdin.readline
#print = sys.stdout.write
result = set()

def fun(step, tmp):
    if step == 0:
        #print(tmp)
        result.add(tuple(tmp))
        return

    for e in nums:
        if used[e]>0:
            tmp.append(e)
            used[e]-=1
            fun(step-1, tmp)
            tmp.pop()
            used[e]+=1

n, m = map(int, input().split())
nums = list(map(int, input().split()))

used = [0 for i in range(10001)]

# 사용된 원소의 개수
for e in nums:
    used[e]+=1


fun(m, [])
result = list(result)
result.sort()

for e in result:
    print(*e)