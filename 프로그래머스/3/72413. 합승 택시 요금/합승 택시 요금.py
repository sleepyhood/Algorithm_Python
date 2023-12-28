INF = 30000000

def floyd(n, dis):
    for w in range(n):
        for i in range(n):
            for j in range(n):
                if dis[i][w] + dis[w][j] < dis[i][j]:
                    dis[i][j] = dis[i][w] + dis[w][j]

def solution(n, s, a, b, fares):
    answer = INF
    dis = [[INF] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dis[i][j] = 0

    for e in fares:
        dis[e[0] - 1][e[1] - 1] = e[2]
        dis[e[1] - 1][e[0] - 1] = e[2]

    floyd(n, dis)

    s -= 1
    a -= 1
    b -= 1

    for i in range(n):
        answer = min(answer, dis[s][i] + dis[i][a] + dis[i][b])

    return answer