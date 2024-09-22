from collections import deque
import sys
#import math 
#import bisect
"""
[백준]
15654. N과 M (5)
https://www.acmicpc.net/problem/15654
"""

input = sys.stdin.readline
print = sys.stdout.write
#math라이브러리 사용


def sol(li, used):
    global m
    global n
    global kinds
    #print(m)

    if len(li) == m:
        res = " ".join(map(str, li))
        print(f"{res}\n")
        return

    # 이전에 선택한 숫자 i부터 시작하여 비내림차순을 유지
    for i in range(len(kinds)):
        if used[kinds[i]]:
            continue

        li.append(kinds[i])
        used[kinds[i]] = 1

        sol(li, used)
        li.pop()  # append된 값 지우는 용도
        used[kinds[i]] = 0  # 사용 해제



n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 자기자신을 제외한 중복 수열

kinds = list(set(arr))
kinds = sorted(kinds)

used = {value: 0 for value in kinds}

sol([], used)