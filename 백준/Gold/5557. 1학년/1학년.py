
n = int(input())

li = list(map(int, input().split()))

# print(li)
dp = [[0] * 21 for _ in range(n-1)] # 마지막 수는 결과값이므로 n-1까지만 필요함

# dp[i][j] = i번째 숫자까지 봤을 때, 결과가 j인 경우의 수


num = li[0]
dp[0][num] = 1  # 1번째 숫자는 만드는 방법은 1가지

# num = li[2]
# if li[1]-num >=0:
#     dp[2][li[1]-num] += dp[1][li[1]]
# if li[1]+num<=20:
#     dp[2][li[1]+num] += dp[1][li[1]]
    

for i in range(1, n-1):         # 마지막 값은 연산에 포함하지 않는다.
    for j in range(21):         # 0~20을 만들기
        if dp[i - 1][j] > 0:    # 이전에 j를 만들 수 있었다면, 다음 숫자를 만드는 방법도 누적된다.
            if j-li[i] >=0:
                dp[i][j-li[i]] += dp[i-1][j]
            if j+li[i]<=20:
                dp[i][j+li[i]] += dp[i-1][j]

lst = li[n-1]

print(dp[n-2][lst])