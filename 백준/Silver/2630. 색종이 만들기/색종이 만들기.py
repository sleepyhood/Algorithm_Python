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
        # 각 구간을 1/2씩 잘라서, 사이즈와 같이 반환
        q1 = quarter(paper, leftX, leftY, size//2)
        q2 = quarter(paper, leftX+size//2, leftY, size//2)
        q3 = quarter(paper, leftX, leftY+size//2, size//2)
        q4 = quarter(paper, leftX+size//2, leftY+size//2, size//2)

        # 모두 같은 값인지 체크
        if q1 == q2 == q3 == q4:
            return q1  # 모두 같은 경우, 해당 값(0 또는 1)을 반환

        # 값이 섞여 있으면 각 구역을 카운팅
        # 삽질 주의: 합을 구해버리면, 어느 구역이 1, 0인지 확인이 불가
        for q in [q1, q2, q3, q4]:
            if q == 1:
                blueCnt += 1
            elif q == 0:
                whiteCnt += 1

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