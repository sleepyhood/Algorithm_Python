"""
[백준]
12065. 단어순서 뒤집기
https://www.acmicpc.net/problem/12605
"""
import sys
from collections import deque

#input = sys.stdin.readline
#print = sys.stdout.write

n = int(input())

for i in range(1, n+1):
    s = input().split()
    print(f"Case #{i}: {' '.join(s[::-1])}")