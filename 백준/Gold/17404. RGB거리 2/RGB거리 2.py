       

n = int(input())
li = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    li.append(tmp)

# 이전색상의 값으로, 전전의 색상이 아닌걸 고르기
"""
3
26 40 83
49 60 57
13 89 99
[26, 40, 83]
[89, 86, 83]

"""
# i번째 선택은, i-1번째의 선택을 제외
# 이 때, n-1번째 선택이 0번째 선택과 달라야 한다.    => 처음 선택에 따라 결과가 바뀌므로, 선택 후 가정

INF = int(1e9)
res = INF

for first_color in range(3):
    # 0: Red
    # 1: Green
    # 2: Blue
    
    dp = [[INF] * 3  for i in range(n)]
    
    # 1번 색상 가정
    dp[0][first_color] = li[0][first_color]

    # N(2 ≤ N ≤ 1,000)

    for i in range(1, n):
        dp[i][0] = li[i][0] + min(dp[i-1][1], dp[i-1][2] )
        dp[i][1] = li[i][1] + min(dp[i-1][0], dp[i-1][2] )
        dp[i][2] = li[i][2] + min(dp[i-1][0], dp[i-1][1] )

    for last_color in range(3):
        if last_color != first_color:
            res = min(res, dp[n-1][last_color])
print(res)



# dp[n-1][0] = if dp[n-2][1]
# dp[n-1][1] =
# dp[n-1][2] = 


# dp[2][0] = li[2][0] + (li[1][1] + li[0][2] if li[1][1] + li[0][2] <  li[1][2] + li[0][1]  else li[1][2] + li[0][1])
# dp[2][1] = li[2][1] + (li[1][0] + li[0][2] if li[1][0] + li[0][2] <  li[1][2] + li[0][0]  else li[1][2] + li[0][0])
# dp[2][2] = li[2][2] + (li[1][1] + li[0][0] if li[1][1] + li[0][0] <  li[1][0] + li[0][1]  else li[1][0] + li[0][1])

# for i in range(3, n):
#     dp[i][0] = li[i][0] + (li[i-1][1] + dp[i-2][2] if li[i-1][1] + dp[i-2][2] <  li[i-1][2] + dp[i-2][1]  else li[i-1][2] + dp[i-2][1])
#     dp[i][1] = li[i][1] + (li[i-1][0] + dp[i-2][2] if li[i-1][0] + dp[i-2][2] <  li[i-1][2] + dp[i-2][0]  else li[i-1][2] + dp[i-2][0])
#     dp[i][2] = li[i][2] + (li[i-1][1] + dp[i-2][0] if li[i-1][1] + dp[i-2][0] <  li[i-1][0] + dp[i-2][1]  else li[i-1][0] + dp[i-2][1])


