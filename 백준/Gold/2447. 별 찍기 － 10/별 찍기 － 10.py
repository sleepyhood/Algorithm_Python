def f(nr, nc, size):
    if size == 3 :      # 더 이상 재귀 불가한 경우, 최소 단위 찍기
        li[nr][nc:nc+3] = '***'
        li[nr+1][nc:nc+3] = '* *'
        li[nr+2][nc:nc+3] = '***'
        return
    
    for i in range(3):
        for j in range(3):
            if i==1 and j ==1:
                continue
            
            rowOffset = (size//3)*i
            colOffset = (size//3)*j
            
            f(nr + rowOffset, nc+colOffset, size//3)
    # f(nr, nc+size//3*2, size//3)
    # f(nr+size//3, nc, size//3)  
    # f(nr+size//3, nc+size//3*2, size//3)      
    # f(nr+size//3*2, nc, size//3) 
    # f(nr+size//3*2, nc+size//3, size//3) 
    # f(nr+size//3*2, nc+size//3*2, size//3) 


n = int(input())
li = [[' ' for _ in range(n)]for _ in range(n)] 

f(0, 0, n)

for i in range(n):
    for j in range(n):
        print(li[i][j], end= '')
    print()