# 사각형은 항상 2승 값으로 생성됨
# 재귀를 사용하기
# 2*2 행렬로 쪼개진 상태에서, 모든 값이 같으면 하나의 값으로 통일
# 재귀가 필요한지를 먼저 보는것이 중요
quadArr = []
zeroCnt = 0
oneCnt = 0

def quadSuqare(topRow, bottomRow, leftCol, rightCol, size):
    global zeroCnt, oneCnt
    # print(f"{topRow}, {bottomRow}, {leftCol}, {rightCol}, {size}")
    tempList = []

    if (size == 2):
        # print(f"{topRow}, {bottomRow}, {leftCol}, {rightCol}, {size}")
        tempZeroCnt = 0
        tempOneCnt = 0
        for i in range(topRow, bottomRow+1):
            for j in range(leftCol, rightCol+1):
                tempList.append(quadArr[i][j])
                if quadArr[i][j]==0:
                    tempZeroCnt+=1
                else:
                    tempOneCnt+=1
                    
        if(len(set(tempList))==1):
            if tempList[0] == 0:
                zeroCnt+=1
            else:
                oneCnt+=1            
        else:
            zeroCnt+=tempZeroCnt
            oneCnt+=tempOneCnt
                    
    elif size > 2:
        for i in range(topRow, bottomRow+1):
            for j in range(leftCol, rightCol+1):
                tempList.append(quadArr[i][j])
        
#         한 가지 원소로만 차있는 경우
        if(len(set(tempList))==1):
            print(f"!{topRow}, {bottomRow}, {leftCol}, {rightCol}, {size}!")
            if tempList[0] == 0:
                zeroCnt+=1
            else:
                oneCnt+=1
#         0과 1이 섞인 경우
        else:
            quadSuqare(topRow, bottomRow-size//2, leftCol, rightCol-size//2, size//2)
            quadSuqare(topRow, bottomRow-size//2, leftCol+size//2, rightCol, size//2)
            quadSuqare(topRow+size//2, bottomRow, leftCol, rightCol-size//2, size//2)
            quadSuqare(topRow+size//2, bottomRow, leftCol+size//2, rightCol, size//2)
            
    
    
    
def solution(arr):
    answer = []
    global quadArr
    
    quadArr = arr[:]

    quadSuqare(0, len(arr)-1, 0, len(arr)-1, len(arr))
    answer.append(zeroCnt)
    answer.append(oneCnt)

    return answer