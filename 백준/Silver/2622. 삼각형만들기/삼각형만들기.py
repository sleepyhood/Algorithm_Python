def sol(n):
    ans = 0
    for i in range(n//3, n // 2 + n%2):  # a를 1부터 n//3까지 반복
        ans+=i - ((n-i)//2)+1-(n-i)%2
    print(ans)

n = int(input())
sol(n)