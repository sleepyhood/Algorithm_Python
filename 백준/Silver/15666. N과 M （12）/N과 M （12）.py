from collections import deque
import sys
#import math 
#import bisect
"""
[백준]
15666. N과 M (12)
https://www.acmicpc.net/problem/15666
"""

input = sys.stdin.readline
print = sys.stdout.write
#math라이브러리 사용


def sol(li, start):
    global m
    global n
    global kinds
    #print(m)
    tmp = li[:]

    if len(li) == m:
        res = " ".join(map(str, li))
        print(f"{res}\n")
        return

    # 이전에 선택한 숫자 i부터 시작하여 비내림차순을 유지
    for i in range(start, len(kinds)):
        li.append(kinds[i])
        sol(li, i)  # i부터 시작하여 같은 숫자도 다시 선택 가능
        li.pop()  # append된 값 지우는 용도



n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.

kinds = list(set(arr))
kinds = sorted(kinds)

# n과 m(2)에서 추가
# 중복을 허용하지 않는 조합
# 각 숫자는 최대 (조합의 수) / (숫자의 종류)만큼 나올 수 있다.
#comb = math.factorial(n)// (math.factorial(n-m))
#maxCnt = comb // n

sol([], 0)