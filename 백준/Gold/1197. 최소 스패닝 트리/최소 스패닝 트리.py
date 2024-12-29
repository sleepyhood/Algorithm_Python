# print("       _.-;;-._")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-;;-._|")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-''-._|")
"""
[백준]
1197. 최소 스패닝 트리
https://www.acmicpc.net/problem/1197
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


v, e = map(int, input().split())
parents = [i for i in range(v+1)]
rank = [0 for i in range(v+1)]

li = []

for _ in range(e):
    tmp = list(map(int, input().split()))
    li.append(tmp)

li.sort(key = lambda x : x[2])
cost = 0

for s, e, w in li:
    if find(parents, s)!= find(parents, e):
        union(s, e)
        cost+=w
    #print(parents)

print(cost)
