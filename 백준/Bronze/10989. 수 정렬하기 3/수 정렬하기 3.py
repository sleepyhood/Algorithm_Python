"""
[백준]
10989. 수 정렬하기 3
https://www.acmicpc.net/problem/10989
"""

import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())

# 미친 메모리
li = [0]*10001

for i in range(n):
    li[int(input().strip())]+=1

for i in range(1, 10001):
    for j in range(li[i]):
        print(str(i)+"\n")