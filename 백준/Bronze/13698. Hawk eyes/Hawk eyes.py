"""
[백준]
13698. Hawk eyes
https://www.acmicpc.net/problem/13698
"""
import heapq
import sys
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

#n = int(input())
#li = list(map(int, input().split()))
s = input()

li = [0 for _ in range(4)]
li[0] = -1
li[3] = 1

for e in s:
    if e=='A':
        li[0], li[1] = li[1], li[0] 
    elif e=='B':
        li[0], li[2] = li[2], li[0] 
    elif e=='C':
        li[0], li[3] = li[3], li[0] 
    elif e=='D':
        li[1], li[2] = li[2], li[1] 
    elif e=='E':
        li[1], li[3] = li[3], li[1] 
    elif e=='F':
        li[2], li[3] = li[3], li[2] 

for i, e in enumerate(li):
    if e==-1:
        print(i+1)
for i, e in enumerate(li):
    if e==1:
        print(i+1)