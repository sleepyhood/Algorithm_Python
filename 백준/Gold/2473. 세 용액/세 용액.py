n = int(input())

li = list(map(int,input().split()))
li.sort()
#print(li)

MIN = 100000000000 *2
resultp, resultL, resultR= 0,0,0
#print(li)
for i in range(1, n-1):
    p = li[i]

    l = 0
    r = n-1

    while l < i < r < n:
        #print(li[l], p, li[r], p + li[l]+li[r])
        if l == i:
            l+=1
            continue
        if r == i:
            r-=1
            continue

        if li[l] + p + li[r] == 0:  # 완전히 0인 경우
            print(li[l] , p , li[r])
            exit()
        

        if MIN > abs(p + li[l] + li[r]):        
            # 단순히 작은값이면, 음수가 붙은 값만 생각됌.
            # 합했을 때, 절대값이 작게 나와야 한다.
            resultp, resultL, resultR = p, li[l], li[r]
            MIN = abs(p + li[l] + li[r])

        if  p + li[l] + li[r] < 0:   # 음수이면 음수 포인터 당기기
            l+=1
        else:                        # 양수이면 양수 포인터 당기기
            r-=1



print(resultL, resultp, resultR)