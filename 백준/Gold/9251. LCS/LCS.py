def lcs_length(str1, str2):
    n = len(str1)
    m = len(str2)
    
    # 2차원 DP 테이블 초기화 (0으로 채움)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # DP 테이블 채우기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:  # 문자가 같을 때
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # 문자가 다를 때
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            # for e in dp:
            #     print(e)
            # print()
    
    return dp[n][m]

# 입력 받기
str1 = input().strip()
str2 = input().strip()

# 결과 출력
print(lcs_length(str1, str2))
