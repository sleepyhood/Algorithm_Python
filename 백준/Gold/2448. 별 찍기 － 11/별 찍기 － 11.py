def f(nr, nc, size):
    if size == 3 :
        li[nr][nc:nc+6] = '  *   '
        li[nr+1][nc:nc+6] = ' * *  '
        li[nr+2][nc:nc+6] = '***** '
        return
    #f(nr, nc, size//2)
    f(nr, nc+size//2, size//2)  # 위 삼각형(절반만큼 오른쪽으로 이동)
    f(nr+size//2, nc, size//2)      # 아래 왼쪽 삼각형
    f(nr+size//2, nc+size, size//2) # 아래 오른쪽 삼각형(크기만큼 오른쪽으로 이동)


n = int(input())
li = [[' ' for _ in range(n*2)]for _ in range(n)] 

f(0, 0, n)

for i in range(n):
    for j in range(n*2):
        print(li[i][j], end= '')
    print()