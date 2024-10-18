"""
[백준]
18870. 좌표 압축
https://www.acmicpc.net/problem/18870
"""

import heapq
import sys
import math
from collections import deque

sys.setrecursionlimit(100000)  # 재귀 한도를 높여줍니다.

# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
INF = float(1e9)
n = int(input())
#n, m = map(int, input().split())

li = list(map(int, input().split()))

# 중복 제거 후, 정렬
tmp = sorted(list(set(li[:])))
dic = {}


# 각 원소값마다 인덱스 부여
# 최소값일수록 더 작은 인덱스가 붙는다.
for i, e in enumerate(tmp):
    dic[e] = i

# 원본값에 대응되는 인덱스값 출력하기
for e in li:
    print(dic[e],end = " ")