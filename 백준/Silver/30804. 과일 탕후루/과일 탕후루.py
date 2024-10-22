"""
[백준]
30804. 과일 탕후루
https://www.acmicpc.net/problem/30804
"""
import heapq
import sys
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

n = int(input())
li = list(map(int, input().split()))

cnt = [0 for _ in range(10)]
kinds = 0               # 현재 총 과일 종류
total = 0               # 현재 총 과일 개수
ans = 0                 # 2종류 이하로 가능한 최대 과일 개수

l = 0

for r in range(n):
    cnt[li[r]] += 1
    if cnt[li[r]] == 1:
        kinds +=1
    total +=1        
    # 과일 종류가 2종류 초과시 왼쪽 포인터 이동
    while kinds > 2:
        cnt[li[l]] -=1
        if cnt[li[l]] == 0:
            kinds-=1
        l+=1
        total-=1
    ans = max(ans, total)

    
print(ans)
""" 
# 기존 삽질 코드
while l <= r:
    # 왼쪽과 오른쪽 둘 중 어느곳을 빼야 유리한지 확인부터 하기
    if kinds<=2:
        ans = max(ans, total)

    if cnt[li[r]] - 1 == 0:
        cnt[li[r]] -=1
        kinds -=1
        r-=1
        total-=1

    elif cnt[li[l]] - 1 == 0:
        cnt[li[l]] -=1
        kinds -=1
        l+=1
        total-=1

    else:
        cnt[li[l]] -=1
        cnt[li[r]] -=1
        l+=1
        r-=1
        total-=2
# 첫번째 구간 슬라이드
for e in li:
    if cnt[e] ==0:  # 처음 세는 것만 종류로
        if kinds + 1 > 2:   # 2종류 초과시
            break
        kinds+=1
    
    total+=1
    cnt[e]+=1       # 과일 인덱스를 개수로 카운트
print(cnt)

ans = total
st = total
l = 0

for i in range(st, len(li)):

    if cnt[li[i]] != 0: # 이전에 먹은 종류라면
        cnt[li[i]] +=1
        total+=1
    else:       # 종류가 늘어나는 상황
        cnt[li[i]] +=1
        cnt[li[l]] -=1
        l+=1

    ans = max(ans, total)
"""


