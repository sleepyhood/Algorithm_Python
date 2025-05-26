
t = int(input())

for _ in range(t):

    n, k = map(int, input().split())

    d = list(map(int, input().split()))
    d.insert(0,0)       # 1번 부터 인덱스

    graph = [[]for i in range(n+1)]     
    indegree = [0]*(n+1)

    for _ in range(k):
        s, e = map(int, input().split())    
        graph[s].append(e)      # 연결
        indegree[e]+=1          # 숫자가 작을수록 시작점

    w = int(input())            # 지어야 할 건물

    q = []
    INF = float(1e9)
    cost = [0] * (n+1)          # 누적되는 최대 시간

    
    for i in range(1, n+1):
        if indegree[i] == 0:    # 출발지 기준
          q.append(i)  
          cost[i] = d[i]


    while q:
        now = q.pop(0)
        #print(cost)
        if now == w:
            break
        for nxt in graph[now]:
            indegree[nxt]-=1
            # 최대값에 맞추어서 계산(같은 레벨이므로)
            if cost[now] + d[nxt] > cost[nxt]:
                cost[nxt]= cost[now] + d[nxt]

            if indegree[nxt] == 0 :
                q.append(nxt)
                

    print(cost[w])