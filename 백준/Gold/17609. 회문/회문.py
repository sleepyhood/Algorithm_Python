n = int(input())
res = []

for _ in range(n):
    str1 = input()
    # 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력해야 한다. 

    l = 0
    r = len(str1)-1
    stack1 = 0

    while l < r:

        if str1[l] == str1[r]:
            l+=1
            r-=1
        else:
            # 유사회문인지 비교 필요.
            # 왼쪽을 옮겨야 맞는지, 오른쪽을 옮겨야 맞는지 검증

            if str1[l+1] == str1[r]: # 왼쪽을 옮기면 괜찮은 경우
                stack1+=1
                l+=2
                r-=1
            elif str1[l] == str1[r-1]: # 오른쪽을 옮기면 괜찮은 경우
                stack1+=1
                l+=1
                r-=2
            else:
                stack1 = 2
                break

    l = 0
    r = len(str1)-1
    stack2 = 0
    while l < r:

        if str1[l] == str1[r]:
            l+=1
            r-=1
        else:
            # 유사회문인지 비교 필요.
            # 왼쪽을 옮겨야 맞는지, 오른쪽을 옮겨야 맞는지 검증

            if str1[l] == str1[r-1]: # 오른쪽을 옮기면 괜찮은 경우
                stack2+=1
                l+=1
                r-=2
            elif str1[l+1] == str1[r]: # 왼쪽을 옮기면 괜찮은 경우
                stack2+=1
                l+=2
                r-=1
            else:
                stack2 = 2
                break
    stack = min(stack1, stack2)
    res.append(stack if stack<=1 else 2)            

for e in res:
    print(e)