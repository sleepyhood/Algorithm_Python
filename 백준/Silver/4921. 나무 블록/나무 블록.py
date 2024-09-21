from collections import deque
"""
[백준]
4921. 나무 블록
https://www.acmicpc.net/problem/4921
"""

# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄에 하나씩 주어진다. 각 조각은 문제의 그림에 나와있는 숫자로 주어진다. 숫자는 공백없이 주어진다. 적어도 1개의 조각이 주어지며, 조각 10,000개를 넘기는 경우는 없다.

# 입력의 마지막 줄에는 0이 하나 주어진다.

cnt = 1

# 해당 블록 바로 오른쪽에 배치 가능한 블록을 value로 저장
# 조건문을 안 쓰고 코드의 가독성을 높이는 방법
# 일종의 파싱 테이블
d = {'1': ['4', '5'], '2':[], '3': ['4', '5'], '4': ['2', '3'], '5': ['8'], '6': ['2', '3'], '7': ['8'], '8': ['6', '7']}


while True:
    b = input()
    q = deque()

    if b == '0':
        break

    isOk = True # 블록을 만들 수 있다고 가정
    
    if b[0]!= '1' or b[-1]!='2':    # 양끝 블록이 올바르지 않은 경우
        isOk = False
    
    else:
        for e in b:
            if len(q)>0:    # 최소한 한 개 이상 들어왔을 때부터 판별 시작
                if not e in d[q[-1]]:
                    isOk = False
                    break
            q.append(e)


    if isOk:
        print(f"{cnt}. VALID")
    else:
        print(f"{cnt}. NOT")

    cnt+=1