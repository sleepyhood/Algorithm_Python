"""
[백준]
1976. 여행 가자
https://www.acmicpc.net/problem/1976
"""

from collections import deque

# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('inf')
INF = 99999999
#input = sys.stdin.readline
#print = sys.stdout.write

def find(parent, node):
    if parent[node] != node:        # 자기 자신이 아니라면
        parent[node] = find(parent, parent[node])   # node의 부모찾기
    return parent[node]

def union(parent, rank, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:    # 서로 다른 부모인 경우
        if rank[root_a] > rank [root_b]:
            parent[root_b] = root_a
        elif rank[root_b] > rank [root_a]:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a
            rank[root_a] += 1


n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
rank = [0 for i in range(n+1)]

for i in range(n):  # 1번부터 n까지 연결 여부
    li = list(map(int, input().split()))
    for j in range(n):    
        if li[j] == 1:
            union(parent, rank, i+1, j+1)
            #print(parent)


q = list(map(int, input().split()))
result = set()
for e in q:
    result.add(parent[e])

# 같은 집합이라면, 부모노드가 같으므로 길이가 1
if len(result) == 1:
    print("YES")
else:
    print("NO")