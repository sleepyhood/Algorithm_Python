"""
[백준]
8896. 가위 바위 보
https://www.acmicpc.net/problem/8896
"""
import heapq
import sys
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

t = int(input())
for _ in range(t):
    n = int(input())
    
    _dict = {}
    li = []

    for i in range(n):
        s = input()
        li.append(s)
        _dict[i+1] = True

    # 열단위로 작업해야함.
    # 승패는 열단위에서 2종류의 패가 나왔을 때만 가능
    rounds = len(li[0])

    for j in range(rounds):
        winOrLose = set()   
        winners = []

        for i in range(n):
            if _dict[i+1]:      # 살아남은 로봇의 승패요소만 수집
                winOrLose.add(li[i][j])

        if len(winOrLose)==2:   # 승패가 나올 수 있는 경우(2가지일 때)
            if 'R' in winOrLose and 'S' in winOrLose:
                for i in range(len(li)):
                    if li[i][j] == 'S': 
                        _dict[i+1] = False      # 진 로봇은 승패 기록용 딕셔너리에 False 처리
            elif 'S' in winOrLose and 'P' in winOrLose:
                for i in range(len(li)):
                    if li[i][j] == 'P':
                        _dict[i+1] = False
 
            elif 'P' in winOrLose and 'R' in winOrLose:
                for i in range(len(li)):
                    if li[i][j] == 'R':
                        _dict[i+1] = False

    #print(_dict)     
    cnt = 0       
    for k in _dict: 
        if _dict[k]:        # 무승부로 남은 로봇 잇는치 탐색
            cnt+=1

    if cnt>1 or cnt==0:               # 무승부가 존재한다면, 로봇은 2개 이상 또는 아예 없는 경우
        print(0)

    else:
        for k in _dict:
            if _dict[k]:
                print(k)
                break