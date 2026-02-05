n= int(input())
lst = list(map(int, input().split()))

cnt = [0]  * 100001


l , r = 0, 0
ans = 0
tmp = 1 # 경우의 수

while l < n and r < n:
    # 1. 오른쪽 값이 기존에 없다면
        # 오른쪽 값 cnt 추가 + 오른쪽 포인터 증가
    if cnt[lst[r]] == 0:
        cnt[lst[r]]+=1
        r+=1

        ans += tmp
        tmp +=1

    # 2. 오른쪽 값이 기존에 있다면
        # 왼쪽 값 cnt 줄이기 + 왼쪽 포인터 증가
        # 이 때, 중복 없을 때까지 왼쪽 포인터 늘려야 함

    elif cnt[lst[r]] != 0:
        cnt[lst[l]]-=1
        l+=1
        tmp = tmp - 1 if tmp > 1 else  1
        
       
    '''        
    print(lst)
    print(f"({l}, {r})")
    print(*cnt[1:6], ans)
    print("=====")
    '''


        
print(ans)