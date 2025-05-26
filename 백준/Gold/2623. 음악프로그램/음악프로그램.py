

n, m = map(int, input().split())

li = [0] * m
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    li[i] = list(map(int, input().split()))
    # li[i][0]이 앞으로 나올 인원 수
    for k in range(1, li[i][0]):
        s = li[i][k]
        e = li[i][k+1]
        #print(s, e)
        graph[s].append(e)
        #if s != e:
        indegree[e]+=1

# print(graph)
# print(indegree)
result = []
q = []

# 시작점부터 만들기
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        result.append(i)


# 위상 정렬 돌리기

while len(q):
    now = q.pop(0)

    for nxt in graph[now]:
        indegree[nxt]-=1
        if indegree[nxt] == 0:
            result.append(nxt)
            q.append(nxt)


# 위상 정렬이 올바른지 검증
if len(result) == n:
    for e in result:
        print(e)
else:
    print(0)