import sys

input = sys.stdin.readline
print = sys.stdout.write

# n이 row, m이 col
N, M = map(int, (input().rstrip()).split())

arr = [['0' for _ in range(M)] for _ in range(N)]

for i in range(N):
    temp = input().rstrip()
    for j in range(M):
        arr[i][j] = temp[j]


minV = 50*50


#lx = -1
ly = -1

# 시작 y좌표를 기준으로, x좌표를 이동하여 최솟값을 구함
while ly+8<N:
    ly+=1
    lx = -1
    while lx+8<M:
        lx+=1
        
        ans1 = 0    # 첫 줄이 bwbw 순일 경우
        ans2 = 0    # 첫 줄이 wbwb 순일 경우
        
        for i in range(ly, ly+8):
            for j in range(lx, lx+8):
                if i%2!=0: # 홀수row
                    if j%2==0: # 짝수col
                        if arr[i][j] == 'B': # 홀수row, 짝수col이 B
                            ans1+=1        
                        else:
                            ans2+=1
                    else: # 홀수col
                        if arr[i][j] == 'W': # 홀수row, 짝수col이 W
                            ans1+=1
                        else:
                            ans2+=1
                
                else: # 짝수row
                    if j%2==0: # 짝수col
                        if arr[i][j] == 'W': # 짝수row, 짝수col이 W    
                            ans1+=1
                        else:   
                            ans2+=1
                    else: # 홀수col
                        if arr[i][j] == 'B': # 짝수row, 홀수col이 B
                            ans1+=1
                        else:
                            ans2+=1

        #print(f"{(ans1, ans2)}\n")
        minV = min(minV, ans1, ans2)
print(f"{minV}\n")