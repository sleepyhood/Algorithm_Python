# 마지막 계단을 밟는다고 가정시, 2가지 경우가 존재
    # n과 n-1, n-3 계단 밟기 
    # n과 n-2 계단 밟기

import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())

dp = [0]*(301)
arr = [0]*(301)

for i in range(n):
    arr[i] = int(input().rstrip())

dp[0] = arr[0]
dp[1] = max(arr[1], arr[0]+arr[1])
dp[2] = max(arr[2]+arr[0], arr[2]+arr[1])

for i in range(3, n):
    dp[i] = max(arr[i] + dp[i-2], arr[i] + arr[i-1] + dp[i-3])

print(f"{dp[n-1]}\n")    
    
    
