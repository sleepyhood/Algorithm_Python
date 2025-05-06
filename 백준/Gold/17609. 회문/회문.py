n = int(input())
res = []

def is_palindrome(l, r):    # 한 칸 이동 후 검증
    while l < r:
        if str1[l] == str1[r]:
            l+=1
            r-=1
        else:
            return False
    
    return True

        

for _ in range(n):
    str1 = input()
    # 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력해야 한다. 

    l = 0
    r = len(str1)-1
    stack = 0

    while l < r:

        if str1[l] == str1[r]:
            l+=1
            r-=1
        else:
            # 유사회문인지 비교 필요.
            # 왼쪽을 옮겨야 맞는지, 오른쪽을 옮겨야 맞는지 검증
            if is_palindrome(l+1, r) or is_palindrome(l, r-1):
                stack = 1
                break
            else:
                stack = 2
                break

    res.append(stack if stack<=1 else 2)            

for e in res:
    print(e)