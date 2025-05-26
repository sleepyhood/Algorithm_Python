from collections import deque
import sys
#import math 
#import bisect
"""
[백준]
9663. N-Queen
https://www.acmicpc.net/problem/9663
"""

# input = sys.stdin.readline
# print = sys.stdout.write
#math라이브러리 사용

def sol(visited, stRow, n):
    #print(visited)
    global cnt
    
    if stRow == n: 
        cnt+=1
        return 

    for col in range(n):      # 열 좌표
        #print(left_dia)
        if visited[col] == False and stRow - col not in left_dia and stRow + col not in right_dia  : # 열이 다른 곳만 탐색하도록
            left_dia.add(stRow - col)
            right_dia.add(stRow+col)
            visited[col] = True            
            sol(visited, stRow+1, n)
            visited[col] = False     
            left_dia.remove(stRow - col)  # Backtrack
            right_dia.remove(stRow + col)  # Backtrack

            # 
        

n = int(input())
#n, m = map(int, input().split())
visited = [False] * (n)     # 방문한 x좌표 표기
left_dia = set()        # 행-열의 값으로 왼쪽 대각선 기울기 저장
right_dia = set()        # 행+열의 값으로 오른쪽 대각선 기울기 저장

cnt = 0

sol(visited, 0, n)

#print(left_dia)
#print(right_dia)
print(f"{cnt}")