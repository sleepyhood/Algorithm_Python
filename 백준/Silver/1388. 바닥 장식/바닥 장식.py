height, width = map(int, input().split())
arr = []
colCnt, rowCnt = 0, 0

for _ in range(height):
    temp = list(input())
    arr.append(temp)


for i in range(height):
    col = 0
    isWidth = False
    
    while col<width:
        isWidth = False
        # col-1 까지 -이면 col 증가
        # 끝이 같다면 상관없지만, 다른 종류면 예외처리
        while col+1<width and arr[i][col] =='-':
            col+=1
            isWidth = True
            
        # 끝자리를 봤는데, 이전에 -와 다른 문자일 경우에는 독립된 타일
        if col == width-1:
            if isWidth == False and arr[i][col] =='-':
                colCnt+=1

        if isWidth:
            colCnt+=1
            isWidth = False

        
        col+=1
    #colCnt+=tempColCnt
    

for i in range(width):
    row = 0
    isHeight = False
    
    while row<height:
        isHeight = False
        # row-1 까지 |이면 row 증가
        # 끝이 같다면 상관없지만, 다른 종류면 예외처리        
        while  row+1<height and arr[row][i] =='|':
            row+=1
            isHeight = True
            
        # 끝자리를 봤는데, 이전에 |와 다른 문자일 경우에는 독립된 타일            
        if row == height-1:
            if isHeight == False and arr[row][i] =='|':
                rowCnt+=1
                
        if isHeight:
            rowCnt+=1
            isHeight=False

        row+=1
    #rowCnt+=tempRowCnt

#print(f"rowCnt: {rowCnt}, colCnt: {colCnt}")    
print(rowCnt+colCnt)
