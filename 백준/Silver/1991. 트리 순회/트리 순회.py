"""
[백준]
1991. 트리 순회
https://www.acmicpc.net/problem/1991
"""

import sys
from collections import deque

# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('inf')
INF = 99999999
#input = sys.stdin.readline
#print = sys.stdout.write

def preorder(node):
    if node != '.':
        print(node, end="")         # 현재 노드 방문
        preorder(tree[node][0])   # 왼쪽 자식 방문
        preorder(tree[node][1])   # 오른쪽 자식 방문


def inorder(node):
    if node != '.': 
        inorder(tree[node][0])  # 왼쪽 자식 방문
        print(node, end="")  # 현재 노드 방문
        inorder(tree[node][1])  # 오른쪽 자식 방문

def postorder(node):
    if node != '.':
        postorder(tree[node][0])  # 왼쪽 자식 방문
        postorder(tree[node][1])  # 오른쪽 자식 방문
        print(node, end="")  # 현재 노드 방문

#n, m = map(int, input().split())
n = int(input())
tree = {}   # 무조건 A노드부터 시작


for i in range(n):
    a,b,c = map(str, input().split())
    # if a not in tree:
    #     tree[a] = []

    # tree[a].append(b)
    # tree[a].append(c)
    tree[a] = [b, c]

preorder('A')
print("")
inorder('A')
print("")
postorder('A')
