from collections import deque
"""
[백준]
9019. DSLR 
https://www.acmicpc.net/problem/9019
"""


T = int(input().rstrip())


for _ in range(T):
    q = deque()
    visited = [""] * 10000   # 방문 여부
    ans = ""    # 명령어 저장

    tmp = input().rstrip()
    a, b = map(int, tmp.split())

    q.append([a, ""])

    while q:
        num , com = q.popleft()

        if num == b:
            print(com)
            break
        
        # D: 2배 후 10000을 나눈 나머지
        if not visited[num*2%10000]:
            visited[num*2%10000]=com+"D"
            q.append([num*2%10000, visited[num*2%10000]])

        # S: -1 연산
        # 주의: n이 0이라면 9999가 대신 들어감
        if num>0 and not visited[num-1]:
            visited[num-1]=com+"S"
            q.append([num-1, visited[num-1]])
        elif num==0 and not visited[9999]:
            visited[9999]=com+"S"
            q.append([9999, visited[9999]])

        lNum = rNum = num

        lNum = (num%1000) * 10 + (num//1000)
        rNum = (num%10) * 1000 + (num//10)
        # 현재 원소가 10보다 크거나 같다면, 뒤집는 연산이 존재
        # if num >= 10:
        #     num = str(num)
        #     lNum = int(num[1:] + num[0])
        #     rNum = int(num[-1] + num[:-1])
        #     while rNum<1000:
        #         rNum*=10

        # L: 가장 왼쪽 원소를 오른쪽으로 옮기기
        if 0<=lNum<10000 and not visited[lNum]:
            #print(f"L: {lNum}")
            visited[lNum]=com+"L"
            q.append([lNum, visited[lNum]])

        # R: 가장 오른쪽 원소를 왼쪽으로 옮기기
        if 0<=rNum<10000 and not visited[rNum]:
            #print(f"r: {rNum}")
            visited[rNum]=com+"R"
            q.append([rNum, visited[rNum]])