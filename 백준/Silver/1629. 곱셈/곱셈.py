"""
[백준]
1629. 곱셈
https://www.acmicpc.net/problem/1629
"""

import heapq
import sys
import math
from collections import deque


sys.setrecursionlimit(100000)  # 재귀 한도를 높여줍니다.

# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
INF = float(1e9)
#n = int(input())

def f(base, n):
    global c
    if n == 0:
        return 1
    if n == 1:
        return base % c
    # 기존 코드: 재귀를 여러번 중복됨
    # if n%2 == 0:
    #     return f(base, n//2) * f(base, n//2)
    # else:
    #     return f(base, n//2)*f(base, n//2)*a

    # 이래와 같이 자신의 절반제곱을 미리 호출하여 곱해주기
    # f(10, 11) → f(10, 5) → f(10, 2) → f(10, 1)
    tmp = f(base, n//2) % c


    if n%2 == 0:
        return tmp * tmp % c
    else:
        return tmp * tmp * a % c


"""
모듈러 연산의 성질:
모듈러 연산은 곱셈과 덧셈에 대해 다음과 같은 성질을 가집니다:

(a×b) mod c = [(a mod c)×(b mod c)] mod c
"""
a, b, c = map(int, input().split())

res = f(a, b)
print(res)