def change(cmd, n, m):
    global li

    # 상하 반전
    if cmd == 1:
        for i in range(0, n//2):
            for j in range(m):
                li[i][j], li[n-i-1][j] = li[n-i-1][j], li[i][j]

    # 좌우 반전
    if cmd == 2:
        for j in range(0, m//2):
            for i in range(n):
                li[i][j], li[i][m-j-1] = li[i][m-j-1], li[i][j]

    # 오른쪽 90도
    if cmd == 3:
        tmp = [[0 for j in range(n)] for i in range(m)]

        for i in range(n):
            for j in range(m):
                tmp[j][n-1-i] = li[i][j]

        li = tmp[:]

    # 왼쪽 90도
    if cmd == 4:
        tmp = [[0 for j in range(n)] for i in range(m)]

        for i in range(n):
            for j in range(m):
                tmp[m-1-j][i] = li[i][j]

        li = tmp[:]

    # 시계방향 부분그룹
    if cmd == 5:
        tmp = [[0 for j in range(m)] for i in range(n)]

        for i in range(0, n//2):
            for j in range(0, m//2):
                tmp[i+0][j+m//2] = li[i][j]
                
        for i in range(0, n//2):
            for j in range(m//2, m):
                tmp[i+n//2][j+0] = li[i][j]
                                
        for i in range(n//2, n):
            for j in range(m//2, m):
                tmp[i][j-m//2] = li[i][j]
                                
        for i in range(n//2, n):
            for j in range(0, m//2):
                tmp[i-n//2][j+0] = li[i][j]

        li = tmp[:]

    # 반시계방향 부분그룹
    if cmd == 6:
        tmp = [[0 for j in range(m)] for i in range(n)]

        for i in range(0, n//2):
            for j in range(m//2, m):
                tmp[i+0][j-m//2] = li[i][j]
                                
        for i in range(n//2, n):
            for j in range(m//2, m):
                tmp[i-n//2][j+0] = li[i][j]
                                
        for i in range(n//2, n):
            for j in range(0, m//2):
                tmp[i][j+m//2] = li[i][j]

        for i in range(0, n//2):
            for j in range(0, m//2):
                tmp[i+n//2][j] = li[i][j]
        li = tmp[:]




n,m,r = map(int, input().split())
li = []

for _ in range(n):
    li.append(list(map(int, input().split())))

cmds = list(map(int, input().split()))


for i in range(r):
    change(cmds[i], len(li), len(li[0]))

for e in li:
    print(*e)
#print("\n\n")