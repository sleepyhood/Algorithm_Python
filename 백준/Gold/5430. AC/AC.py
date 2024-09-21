"""
[백준]
5430. AC
https://www.acmicpc.net/problem/5430
"""
import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

# 핵심: reserve가 시간을 많이 소요하므로 앞인지 뒤인지를 따질것
T = int(input().rstrip())
for _ in range(T):
    com = list(input().rstrip())
    # 두 가지 함수 R(뒤집기)과 D(버리기)
    n = int(input().rstrip())
    # 배열에 들어있는 수의 개수 n
    
    _list = input().rstrip()
    _list = _list[1:-1].split(',')
    
    dq = deque()
    if _list and n>0:
        dq = deque(_list)
    elif n ==0:
        dq = []
        
    isError = False
    isReverse = 0
    for c in com:
        if c == "R":
            #dq.reverse()
            isReverse+=1
            #_list = _list[::-1]
            
        elif c == "D":    # c=="D"
            if len(dq)>0: # 아이템이 존재하는 경우
                #del _list[0]
                if isReverse%2==0:
                    dq.popleft()
                else:
                    dq.pop()
                #isReverse = 0
            else:
                print("error\n")
                isError = True
                break
    if not isError:
        str_list = list(dq)
        int_list = [int(x) for x in str_list]

        if isReverse%2!=0:
            int_list = int_list[::-1]
        
        # 삽질의 주범
        # 결과값에서, 쉼표마다 공백은 없으므로 직접 반복문으로 출력해야함
        # 또한, 비어있는 리스트도 고려해야함
        # 첫번째 if는 원소가 2개 이상일때만 잘 작동함...
        if len(int_list) >= 2:
            for i, e in enumerate(int_list):
                if i == 0:
                    print(f"[{e},")
                elif i == len(int_list)-1:
                    print(f"{e}]\n")
                else:
                    print(f"{e},")
        
        elif len(int_list) >= 1:
            print(f"[{int_list[0]}]\n")

        else:
            print(f"[]\n")