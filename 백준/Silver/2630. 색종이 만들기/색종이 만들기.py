"""
[백준]
2630. 색종이 만들기
https://www.acmicpc.net/problem/2630
"""

import heapq
import sys
import math
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

#n, m, d = map(int, input().split())

# 크기가 4 이상이면 계속 재귀하지만, 2일 때 부터 같은 면인지를 리턴
# 모두 1이면, n크기의 구간의 합은 n**2

"""
4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1

4
1 0 0 0
0 1 0 0
0 0 1 1
0 0 1 1
"""

def quarter(paper, leftX, leftY, size):
    global whiteCnt
    global blueCnt
    if size == 1:
        #(f"leftX: {leftX}\tleftY: {leftY}\t{paper[leftY][leftX]}")
        return paper[leftY][leftX]
    
    else:    # 재귀가 필요
        q1 = quarter(paper, leftX, leftY, size//2)
        q2 = quarter(paper, leftX+size//2, leftY, size//2)
        q3 = quarter(paper, leftX, leftY+size//2, size//2)
        q4 = quarter(paper, leftX+size//2, leftY+size//2, size//2)

        # 모두 같은 값인지 체크
        if q1 == q2 == q3 == q4:
            return q1  # 모두 같은 경우, 해당 값(0 또는 1)을 반환
        else:
            # 값이 섞여 있으면 해당 구역을 카운팅
            if q1 == 1: blueCnt += 1
            if q2 == 1: blueCnt += 1
            if q3 == 1: blueCnt += 1
            if q4 == 1: blueCnt += 1
            if q1 == 0: whiteCnt += 1
            if q2 == 0: whiteCnt += 1
            if q3 == 0: whiteCnt += 1
            if q4 == 0: whiteCnt += 1
            return -1  # 혼합된 경우, -1 반환 (이 값은 상위에서 처리 안 함)
        

N = int(input())

paper = []

for _ in range(N):
    paper.append(list(map(int, (input().rstrip()).split())))

whiteCnt = 0
blueCnt = 0
            
res = quarter(paper, 0, 0, N)    
    
# 전체가 1또는 0인 경우
if res == 1:
    blueCnt+=1
elif res == 0:
    whiteCnt+=1

print(whiteCnt)
print(blueCnt)