"""
[백준]
12904. A와 B
https://www.acmicpc.net/problem/12904
"""

from collections import deque
import heapq
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('inf')
INF = 99999999
#input = sys.stdin.readline
#print = sys.stdout.write

"""
AAB

BAABAA
AABAABBAAAAAAAA
"""

s = input()
t = input()

#t = t.replace(s,'@', 1)
t = [str(i) for i in t]
#print(t)

while len(t)>1:
    isRemove = False

    if ''.join(t) == s:
        break
    elif t[-1] == 'A':
        t.pop()
        isRemove = True
    
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
        isRemove = True

    if not isRemove:
        break
    

#print(t)

if ''.join(t) == s:
    print(1)
else:
    print(0)