# print("       _.-;;-._")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-;;-._|")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-''-._|")
"""
[백준]
8980. 택배
https://www.acmicpc.net/problem/8980
"""

"""
1 2 30		1	30	
3 4 40		1	40	
2 5 70		3	60	
5 6 60		1	60	
1 6 40		5	30	
"""

from collections import deque
import heapq

# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('inf')
INF = 99999999
#input = sys.stdin.readline
#print = sys.stdout.write


n, c = map(int, input().split())
m = int(input())    # 박스 정보

li = []
for i in range(m):
    li.append(list(map(int, input().split())))

li.sort(key = lambda x:x[1])  # 도착하는 곳 우선적으로 정렬
total = 0
capacity = [0 for i in range(n+1)]  # 각 마을 별 담긴용량
# 이 때, 택배는 출발지에만 반영

for i in range(m):
    st = li[i][0]
    ed = li[i][1]
    box = li[i][2]
    maxLoad = 0

    # 시작지점부터 끝까지 최대로 적재된 곳 찾기
    for j in range(st, ed):
        maxLoad = max(maxLoad, capacity[j])
    
    # 실제로 적재 가능한 양 찾기
    # 최대로 적재되었다면, 해당 구간은 더 이상 택배를 못 넣는다.
    available = min(box, c - maxLoad)
    total += available

    # 해당 구간 반영
    for j in range(st, ed):
        capacity[j] += available
#print(li)
print(total)