# https://www.acmicpc.net/problem/28325
"""
개미들은 똑똑하기 때문에, 이 조건을 만족하는 하에 최대한 많은 수의 개미들이 현재 개미굴에 살고 있다고 한다. 
현재 개미굴의 구조가 주어질 때, 개미굴에 살고 있는 개미의 수를 구하는 프로그램을 작성하라
"""

# 쪽방이 있다면, 항상은 아니지만 쪽방에 있는 편이 유리하다.
# 쪽방을 사용한다면, 쪽방 모두를 선택하는 선택지이다.

# 쪽방이 있다면, 인접한 방을 선택할 수 있다.
# 0 0 -> 방 1개
# 2 0 -> 쪽방 2개
# 1 1 -> 쪽방 2개(1개씩)
# 8 1 -> 쪽방 8+1


n = int(input())

li = list(map(int, input().split()))
li = [0] + li

# 시작과 끝 비교
# 1번방을 선택하냐, 선택하지 않냐

# 이전 방이 쪽방 -> 현재 방 선택 
# 이전 방이 쪽방아님-> 내가 쪽방이면 선택, 아니면 그냥 +1


# 내가 처음에 무엇을 선택하냐에 따라 결과가 바뀜
# 첫번째 혹은 마지막에 쪽방은 상관없으나, 둘다 일반 방이면 문제가 됌.


result = 0
for firstChoice in range(3):
    dp = [[0]*3 for i in range(n+1)]

    if firstChoice == 0:
        dp[1][0] = 0
    elif firstChoice == 1:
        dp[1][1] = 1
    elif firstChoice == 2:
        dp[1][2] = li[1]    

    for i in range(2, n+1):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + 1
        dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + li[i]

    for last_choice in range(3):
        if not(firstChoice==1 and last_choice==1):  # 둘다 그냥 방 선택은 안됌
            result = max(result, dp[n][last_choice])
print(result)

