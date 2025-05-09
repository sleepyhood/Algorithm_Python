n, k = map(int, input().split())
coins = [0] * (n+1)

for i in range(1, n+1):
    coins[i] = int(input())
    

dp = [0] * (k+1) 
dp[0] = 1

for coin in coins:
    for j in range(coin, k+1):
        dp[j] += dp[j - coin]

print(dp[k]//2)