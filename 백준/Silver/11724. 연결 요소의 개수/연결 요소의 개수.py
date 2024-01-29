import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
print = sys.stdout.write


N, M = map(int, (input().rstrip()).split())

graph = {}
visited = [False]*(N+1)

for _ in range(M):
    u, v = map(int, (input().rstrip()).split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)
#{1: [2, 5], 2: [1, 5], 5: [2, 1], 3: [4], 4: [3, 6], 6: [4]}



group = 0

def dfs(key, graph, visited):
    
    visited[key] = True
    if key in graph:    # 존재하는 노드일 경우
        for i in graph[key]:    # 노드의 values에 접근
            #print(f"{i}: {visited[i]}\n")
            if not visited[i]:    # 아직 미방문시
                #group+=1
                #visited[i] = True
                dfs(i, graph, visited)# visited 여부가 아닌, 인덱스 값을 전달(false인 인덱스도 방문)
                #group+=1


# 만약 현재 방문한 노드가 기존에도 있을 시, 같은 번호로 연결
for i in range(1, N+1):
    #print(f"{visited}\t")
    if not visited[i]: # 미방문 노드
        dfs(i, graph, visited)
        group+=1

    #print(f"\ngroup: {group}\n")
            
    # print(f"{i}: {visited[i]}\n")

#print(f"\n{visited}\n")

#print(f"\n{group}\n")


print(f"{group}\n")
