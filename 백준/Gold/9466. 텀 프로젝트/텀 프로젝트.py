import sys
sys.setrecursionlimit(10 ** 5)

def dfs(node):
    
    global graph
    global visit
    global finished
    global result

    visit[node] = True

    nxt = graph[node][0]
    #print(f"st: {st}\t node: {node}")
    if not visit[nxt]:  # 한 번도 본적 없다면
        dfs(nxt)
    elif not finished[nxt]: # 사이클이 있는지 확인하지 못했다면

        tmp = nxt
        cnt = 1

        while tmp != node:  # 자기자신한테 오도록 방문
            tmp = graph[tmp][0]
            cnt+=1

        result+= cnt
    finished[node]  = True


t = int(input())

for _ in range(t):

    n = int(input())

    li = list(map(int, input().split())) 
    li.insert(0,0)  # 0번 인덱스 맞추기

    graph = [[]for i in range(n+1)]

    for i in range(1, n+1):
        graph[i].append(li[i])
    
    # 팀을 맺으려면, 각 번호마다 순회시 자기 자신으로 돌아올 수 있다.
    visit = [0] * (n+1)     # 방문 여부
    finished = [0] * (n+1)  # 사이클 여부
    
    result  = 0
    for i in range(1, n+1):
    
        if not visit[i]:
            dfs(i)
            #visit[i] = 0

    print(n - result)
