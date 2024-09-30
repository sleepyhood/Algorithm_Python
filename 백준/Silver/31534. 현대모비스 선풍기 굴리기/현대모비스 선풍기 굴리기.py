"""
[백준]
31534. 현대모비스 선풍기 굴리기
https://www.acmicpc.net/problem/31534
"""

import heapq
import sys
import math
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

#t = int(input())
#m = int(input())
#li = list(map(int, input().split()))

a, b, h = map(int, input().split())

if a > b:
    a, b = b, a

# 사다리꼴을 연장하여, 높이를 x라 가정
# ▷ 이 때, 2가지 형태의 삼각형은 비례가 존재
# 밑변이 b, 높이가 x vs 밑변이 a, 높이가 x-h
# 이 때, x는 a : b = (x-h):x -> b(x-h) = ax-> bx-bh = ax-> x(b-a) = bh -> x = bh / (b-a)

x = b*h / (b-a)

# 밑변이 a인 빗변의 길이: ((h-x)^2+a^2)**0.5
s1 = ((x-h)**2+a**2)**0.5

# 밑변이 b인 빗변의 길이: ((x)^2+a^2)**0.5
s2 = ((x)**2+b**2)**0.5

res = (s2**2)*math.pi - (s1**2)*math.pi
print(res)
