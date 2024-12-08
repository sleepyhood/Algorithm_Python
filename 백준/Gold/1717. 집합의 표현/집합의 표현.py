"""
[백준]
1717. 집합의 표현
https://www.acmicpc.net/problem/1717
"""

from collections import deque

# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('inf')
INF = 99999999
#input = sys.stdin.readline
#print = sys.stdout.write


def find(parent, x):
    if parent[x]!=x:    # 루트노드가 아닌 경우
        # 기본값은 자기자신(부모)임
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):  # 합집합 연산
    # 각각 노드의 부모 노드를 조회
    rootA = find(parent, a) # a의 부모노드
    rootB = find(parent, b) # b의 부모노드

    if rootA != rootB:  # 루트가 다른 경우
        if rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        elif rank[rootB] < rank[rootA]:
            parent[rootB] = rootA
        else:
            parent[rootB] = rootA   # b의 부모노드를 a로 설정
            rank[rootA]+=1
        

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [0 for i in range(n+1)]

for _ in range(m):
    q, a, b = map(int, input().split())
    if q==0:
        union(parent, rank, a, b)
        #print(*parent)
        #print(*rank)
    else:
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")

#print(li)