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

n = int(input())    # "IO" 패턴의 개수
m = int(input())    # 문자열의 길이
#li = list(map(int, input().split()))
s = input()         # 주어진 문자열

ans = 0
cnt = 0
i = 0

# 슬라이딩 윈도우를 사용하여 찾기
while i < m-1:
    if s[i:i+3] == "IOI":
        cnt += 1
        if cnt == n:
            ans+=1
            cnt -= 1
        i+=2

    else:
        cnt = 0
        i+=1

print(ans)

"""기존 방식: 문자열 그대로 찾기"""
"""
IOI = ""

for _ in range(n):
    IOI+="IO"
IOI+="I"
#print(IOI)

for i in range(m-len(IOI)+1):
    if s[i]==s[i+1]:
        continue
    if s[i:i+len(IOI)] == IOI:
        ans+=1
print(ans)
"""