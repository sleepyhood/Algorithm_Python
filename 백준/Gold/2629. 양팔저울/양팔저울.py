n = int(input())
li = list(map(int, input().split()))
sumWeight = sum(li)

k = int(input())
querys = list(map(int, input().split()))


dp = [[0]*(sumWeight + 1) for i in range(n+1)]

dp[0][0] = 1 # 0g은 무조건 만들 수 있다.


for i in range(n):

    for j in range(sumWeight+1):

        if dp[i][j]:    # 0g 만든 것부터 시작, 0개씩 쓰는 건 모두 가능하다.
            dp[i+1][j] = 1

            if j + li[i] <= sumWeight:
                dp[i+1][j + li[i]] = 1
            
            if abs(j - li[i]) >= 0:
                dp[i+1][abs(j - li[i])] = 1

# print(dp)
for e in querys:
    if e <= sumWeight and dp[n][e]:
        print("Y", end=' ')
    else:
        print("N", end=' ')