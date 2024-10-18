"""
[백준]
23968. 알고리즘 수업 - 버블 정렬 1
https://www.acmicpc.net/problem/23968
"""

n, k = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
isFind = False

if n**2 < k :   # 교환횟수는 최대 n^2, k가 그보다 크다면 정답 못 찾음
    cnt = -1

else:
    # 버블 정렬 수행
    for i in range(len(li)-1, -1, -1):
        for j in range(i):
            if li[j] > li[j+1]: # 오름차순으로 바꿀 수 있는 경우
                cnt+=1
                li[j], li[j+1] = li[j+1], li[j] 
                if cnt == k:    # 교환횟수를 찾을 경우
                    isFind = True
                    print(li[j] , li[j+1])
                    break
            
                #print("--------------------")
                #print(*li)
            
if not isFind:  # 삽질: 초기에 교환횟수가 너무 크거나, 교환횟수를 못 찾을 경우 -1
    print(-1)