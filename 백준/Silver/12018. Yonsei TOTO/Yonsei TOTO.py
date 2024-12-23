# print("       _.-;;-._")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-;;-._|")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-''-._|")
"""
[백준]
12018. Yonsei TOTO
https://www.acmicpc.net/problem/12018
"""

from collections import deque
import heapq
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('inf')
INF = 99999999
#input = sys.stdin.readline
#print = sys.stdout.write


n, m = map(int, input().split())
mile = []
# 마일리지는 최소한으로 쓰면서, 수강인원에 들어가게끔
for i in range(n):
    p, l = map(int, input().split())
    li = list(map(int, input().split()))
    
    if p < l:   # 사람이 수강 인원보다 적은 경우
        # 1원만 사용해도 참여가능
        mile.append(1)
    else:   # 이미 정원이 있는 경우
        # 예를 들어 5명 신청 + 4명 수강정원이면,
        # 내림차순 정렬 후, 4번째 마일리지와 같은 것으로 대체
        # 같아도 성준이에게 우선순위가 부여된다.
        li.sort(reverse=True)
        mile.append(li[l-1])

mile.sort()

cnt = 0 # 수강과목 수
s = 0   # 사용한 마일리지
for e in mile:
    if s + e <= m:  # 마일리지가 남았다면
        s+=e
        cnt+=1
print(cnt)
