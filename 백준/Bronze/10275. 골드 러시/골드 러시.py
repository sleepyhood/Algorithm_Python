"""
[백준]
10275. 골드 러시
https://www.acmicpc.net/problem/10275
"""

import heapq
import sys
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

# 10진법->2진법 문자열 리턴
def dec2Bin(n, byte):
    res = [0 for _ in range(byte)]
    n = int(n)

    while n>0:
        byte-=1
        res[byte] = n%2
        n//=2
    #res = list(map(str, res))
    #return ''.join(res)
    return res        

t = int(input())
#m = int(input())
#li = list(map(int, input().split()))

for _ in range(t):
    n, a, b = map(int, input().split())
    days = 0
    # a+b=2^n

    # 가방에 담으려면 가장 최소값에 기준에 맞추기
    _min = min(a,b)
    
    golds = 2**n

    
    bina = dec2Bin(_min, n)
    
    idx = n-1

    while bina[idx]==0:
        idx-=1
    print(idx+1)
    # while golds>_min:
    #     golds//=2
    #     days+=1

    # print("golds: ", golds)
    # if _min-golds>0:
    #     golds//2
    #     days+=1
    # print(days)