# 누적합을 저장하는 2차원 배열이 필요
# 즉, 현재의 최대값은 [row-1][col-1]과 [row-1][col+1] 중 선택

import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())

triList = [[0 for _ in range(n)] for _ in range(n)]
sumList = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    temp = list(map(int, (input().rstrip()).split()))
    for j in range(i+1):
        triList[i][j] = temp[j]

sumList = triList[:]     
        
# 첫줄은 볼필요 없음    
for i in range(1, n):
    for j in range(i+1):
        if j==0:
            sumList[i][0] = sumList[i][0] + sumList[i-1][0]
        elif j==i:
            sumList[i][j] = sumList[i][j] + sumList[i-1][j-1]
        else: # 중간값, max 값을 비교하여 저장
            sumList[i][j] = sumList[i][j] + max(triList[i-1][j-1], triList[i-1][j])
            
maxV = max(sumList[n-1][:])
print(f"{maxV}\n")