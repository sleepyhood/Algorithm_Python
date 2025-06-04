from collections import deque

t = int(input())

for _ in range(t):
    input()
    r, c = map(int, input().split())

    li = [0]*r
    q = deque()

    for i in range(r):
        li[i] = list(input())
        for j in range(c):
            if li[i][j] == 'o':
                q.append([i,j])

    
    cnt = 0

    while len(q):
        nr, nc = q.popleft()

        # 가로 체크
        if nc-1>= 0 and nc+1<c and li[nr][nc-1] == '>' and li[nr][nc+1] == '<':
            cnt+=1
        # 세로 체크
        elif nr-1>= 0 and nr+1<r and li[nr-1][nc] == 'v' and li[nr+1][nc] == '^':
            cnt+=1

    print(cnt)