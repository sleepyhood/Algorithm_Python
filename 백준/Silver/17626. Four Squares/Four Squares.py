n = int(input())

# dp[1] = 1^2                           -> 1
# dp[2] = 1^2 + 1^2                     -> 2
# dp[3] = 1^2 + 1^2 + 1^2               -> 3
# dp[4] = 1^2 + 1^2 + 1^2 + 1^2, 2^2    -> 1
# dp[5] = 2^2 + 1^2                     -> 2                 
# dp[6] = 1^2 + 1^2 + 2^2               -> 3
# dp[7] = 1^2 + 1^2 + 1^2 + 2^2         -> 4
# dp[8] = 2^2 + 2^2                     -> 2
# dp[9] = 1^2 + 2^2 + 2^2, 3^2          -> 1


# dp[25] = 4^2 + 3^2, 5^2
dp = [0] * (n+1)
dp[0] = 0
for i in range(1, n + 1):
    dp[i] = float('inf')
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i - j*j] + 1)

print(dp[n])