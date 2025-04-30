
# print("       _.-;;-._")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-;;-._|")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-''-._|")
"""
[백준]
4386. 별자리 만들기
https://www.acmicpc.net/problem/4386
"""

import heapq

def find(parents, node):
    if parents[node] != node:
        parents[node] = find(parents, parents[node])
    return parents[node]

def union(a, b):
    rootA = find(parents, a)
    rootB = find(parents, b)

    if rootA!= rootB:
        if rank[rootB] < rank[rootA]:
            parents[rootB] = rootA
        elif rank[rootA] < rank[rootB]:
            parents[rootA] = rootB
        else:
            parents[rootB] = rootA
            rank[rootA]+=1


n = int(input())
#v, e = map(int, input().split())
parents = [i for i in range(n+1)]
rank = [0 for i in range(n+1)]

li = []

for _ in range(n):
    tmp = list(map(float, input().split()))
    li.append(tmp)

stars = []
# 서로 다른 별자리의 거리 저장
for i in range(n):
    for j in range(i+1, n):
        #if i == j:
        #    continue
        x1 = li[i][0]
        y1 = li[i][1]

        x2 = li[j][0]
        y2 = li[j][1]

        dist = ((x2-x1)**2+(y2-y1)**2)**0.5
        stars.append((i+1, j+1, dist))
        stars.append((j+1, i+1, dist))

# for e in stars:
#     print(e)



stars.sort(key = lambda x : x[2])  # 거리가 짧은 곳부터 탐색
cost = 0

for s, e, w in stars:
    if find(parents, s)!= find(parents, e): # 서로소인 노드일 경우, 묶기
        union(s, e)
        cost+=w
    #print(parents)

print("%.2f"%(cost))
