import math as m
users = [0] * 502 # 마지막 스테이지 인원도 고려

# 전체 스테이지의 개수 N
# 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.
# 주의: 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의
def solution(N, stages):
    answer = []
    
    # 각 stage별 실패 인원을 배열로
    # 예. [2, 1, 2, 6, 2, 4, 3, 3]에서, 
    # 2번 스테이지는 3명 실패(users[2]==3)
    
    for i in stages:
        users[i] += 1
    
#     실패율 계산(1~N+1)
    failPer = [0]*(N+1)
    userCnt = len(stages)
    
    for i in range(1, N+1):
        if userCnt<=0:
            break
        # print(f"i: {i:^5} | failPer: {users[i]/userCnt:^5} | userCnt: {userCnt:^5}")
        if users[i] == 0:
            failPer[i] = 0
            continue

        failPer[i] = (users[i]/userCnt)
        userCnt -=users[i]

    # for i in range(1, N+1):
    #     print(f"i: {i:^5} | failPer: {failPer[i]:^5}")
    
    for i in range(N+1):
        maxIdx = failPer.index(max(failPer))
        if maxIdx==0:
            failPer[maxIdx] = -100
            i-=1
            continue

        answer.append(maxIdx)
        failPer[maxIdx] = -1
    return answer