"""
[백준]
15652. N과 M (4)
https://www.acmicpc.net/problem/15652
"""
import sys

sys.setrecursionlimit(10000)

# 리스트, 최대길이, 재귀횟수, 시작번호

def f(li, n, m, st):
    if m == 0:
        print(*li)
        return
    
    for i in range(st, n+1):
        li.append(i)
        f(li, n, m-1, st)
        li.pop()
        st+=1

n, m = map(int, input().split())
li = []
f(li, n, m, 1)