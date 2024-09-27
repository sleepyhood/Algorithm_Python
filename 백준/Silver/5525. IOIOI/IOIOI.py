"""
[백준]
5525. IOIOI
https://www.acmicpc.net/problem/5525
"""

import heapq
import sys
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

n = int(input())
m = int(input())
#li = list(map(int, input().split()))
s = input()

IOI = ""

for _ in range(n):
    IOI+="IO"
IOI+="I"
#print(IOI)

ans = 0
for i in range(m-len(IOI)+1):
    if s[i:i+len(IOI)] == IOI:
        ans+=1
print(ans)