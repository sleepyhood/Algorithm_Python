"""
[백준]
1874. 스택 수열
https://www.acmicpc.net/problem/1874
"""

import heapq
import sys
import math
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

#n, m = map(int, input().split())

n = int(input())

st = deque()    # 수열
li = deque()    # 입력값
tmp = deque()  
res = []        # 부호 결과값
visit = [0] * (n+1)

visit[0] = 1

for i in range(1, n+1):
    st.append(i)

for _ in range(n):
    li.append(int(input()))


# 1단계: 스택에 최대한 다 넣어보기
while len(st):
    if len(tmp) and tmp[-1] == li[0]:
        res.append('-')
        tmp.pop()
        li.popleft()

    elif len(st):
        res.append('+')
        tmp.append(st[0])
        st.popleft()

    # print(f"li: {li}")
    # print(f"tmp: {tmp}")
    # print(f"st: {st}")
    # print(f"res: {res}")
    # print()

# 2단계: tmp에 남은 원소들 li로 비워보기

while len(tmp):
    if tmp[-1] == li[0]:
        tmp.pop()
        res.append('-')
        li.popleft()
    else:
        break
    
if len(tmp) == 0 and len(li) == 0:  # 완전히 비울 경우
    for e in res:
        print(e)
else:
    print("NO")