n = int(input())

li = list(map(int,input().split()))
li.sort()
#print(li)

l = 0
r = n-1
MIN = 1000000000 *2

resultL = li[l]
resultR = li[r]


while l < r and r < n:
    #print(li[l], li[r], li[l]+li[r])

    if li[l] + li[r] == 0:  # 완전히 0인 경우
        print(li[l], li[r])
        exit()
        

    if MIN > abs(li[l] + li[r]):        
        # 단순히 작은값이면, 음수가 붙은 값만 생각됌.
        # 합했을 때, 절대값이 작게 나와야 한다.
        resultL, resultR = li[l], li[r]
        MIN = abs(li[l] + li[r])

    if li[l] + li[r] < 0:   # 음수이면 음수 포인터 당기기
        l+=1
    else:                   # 양수이면 양수 포인터 당기기
        r-=1


print(resultL, resultR)