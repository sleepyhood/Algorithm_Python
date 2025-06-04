n = int(input())

li = list(map(int, input().split()))

# 마지막은 무조건 1, 그다음은 2, ... 감속을 기준으로 잡기

speed = 0
total = 0

for i in range(n-1, -1, -1):
    if li[i] > speed:
        speed+=1
    else:
        speed = li[i]
    
    total+=speed
print(total)