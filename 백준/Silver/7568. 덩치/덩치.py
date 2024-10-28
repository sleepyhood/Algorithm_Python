"""
[백준]
7568. 덩치
https://www.acmicpc.net/problem/7568
"""

import sys
import heapq
#input = sys.stdin.readline
#print = sys.stdout.write

n = int(input().strip())

li = []

for i in range(n):
    li.append(list(map(int, input().split())))

grade = [0]*n

for i in range(n):
    tmp = 1
    for j in range(n):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            tmp+=1
    grade[i] = tmp

print(*grade)