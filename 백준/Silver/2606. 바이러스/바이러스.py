import sys

input = sys.stdin.readline

N = int(input().rstrip())
C = int(input().rstrip())

#arr = [[0 for i in range(N+1)] for j in range(N+1)]

graph = {}
visited = [0 for _ in range(N+1)]

for _ in range(C):
    com1, com2 = map(int, (input().rstrip()).split())
    
    if com1 not in graph:
        graph[com1] = []
    if com2 not in graph:
        graph[com2] = [] 
    graph[com1].append(com2)
    graph[com2].append(com1)
#print(graph)   
# {1: [2, 5], 2: [1, 3, 5], 3: [2], 5: [1, 2, 6], 6: [5], 4: [7], 7: [4]}


def dfs(key):
    visited[key] = 1 # 처음 들어온것도 확인
    if key in graph:# 키 유무를 먼저 확인
        for val in graph[key]:# key에 대응되는 values
            if visited[val] == 0:
                visited[val] = 1
                dfs(val)
            
#virus = set()
dfs(1)
#print(virus)
print(f"{sum(visited)-1}\n")            
#print(f"{result}\n")   