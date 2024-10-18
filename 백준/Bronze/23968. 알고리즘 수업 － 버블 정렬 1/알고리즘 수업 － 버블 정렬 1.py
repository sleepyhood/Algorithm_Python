"""
[백준]
23968. 알고리즘 수업 - 버블 정렬 1
https://www.acmicpc.net/problem/23968
"""

n, k = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
isFind = False

if n**2 < k :
    cnt = -1

else:
    for i in range(len(li)-1, -1, -1):
        for j in range(i):
            if li[j] > li[j+1]:
                cnt+=1
                li[j], li[j+1] = li[j+1], li[j] 
                if cnt == k:    # 교환횟수를 찾을 경우
                    isFind = True
                    print(li[j] , li[j+1])
                    break
            
                #print("--------------------")
                #print(*li)
            
if not isFind:
    print(-1)