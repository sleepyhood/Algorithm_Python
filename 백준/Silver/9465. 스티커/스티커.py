t = int(input())

for _ in range(t):
    n = int(input())
    li = []
    li.append(list(map(int, input().split())))
    li.append(list(map(int, input().split())))
        
    dp = [[0]*3 for i in range(n)]
    
    # 스티커를 떼는 경우는 3가지
    # 0. 현재 스티커를 떼지 않는다. = max(i-1번째에 위쪽 스티커 최대값,  i-1번째에 아래쪽 스티커 최대값)
    # 1. 위쪽 스티커 떼기 + max(i-1번째에 위쪽 스티커를 안 뗌,  i-1번째에 아래쪽 스티커를 뗌)
    # 2. 아래쪽 스티커 떼기 + max(i-1번째에 아래쪽 스티커를 안 뗌,  i-1번째에 위쪽 스티커를 뗌)
    
    dp[0][0] = 0    # 사실 dp[i-2]까지의 최대값
    dp[0][1] = li[0][0] # 위 행의 데이터 선택시
    dp[0][2] = li[1][0] # 아래 행의 데이터 선택시
    
    
    # dp[1][0] = max(dp[0][1], dp[0][2])
    # dp[1][1] = max(li[0][1] + dp[0][0], li[0][1] + dp[0][2])
    # dp[1][2] = max(li[1][1] + dp[0][0], li[1][1] + dp[0][1] )
    
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = li[0][i] + max(dp[i-1][0] , dp[i-1][2])
        dp[i][2] = li[1][i] + max(dp[i-1][0],  dp[i-1][1])

    print(max(dp[-1][0], dp[-1][1], dp[-1][2]))

    
