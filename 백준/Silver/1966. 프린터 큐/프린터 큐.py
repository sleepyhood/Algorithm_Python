"""
[백준]
1966. 프린터 큐
https://www.acmicpc.net/problem/1966
"""

import heapq
import sys
import math
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write


# 입력    
t = int(input())

for _ in range(t):
    # 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)
    # 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)
    N, M = map(int, input().split())
    
    #arr = input().rstrip()
    arr = list(map(int, input().split()))
    # 현재 M 번째 문서가 실제로 출력되는 시점을 출력
    
    step = 1
    while len(arr)>0:
        if arr[M] == max(arr) and M == 0:
            # 첫번째로 출력되는 문서인 경우
            break
        elif max(arr) == arr[0]:
            step+=1
            del arr[0]
            M-=1
            if M<0:
                M = len(arr)-1
        else:
            #step += 1
            temp = arr.pop(0)
            arr.append(temp)
            M-=1
            if M<0:
                M = len(arr)-1
    print(f"{step}")       