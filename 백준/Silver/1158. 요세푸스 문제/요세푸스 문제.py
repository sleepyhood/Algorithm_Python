N, K = map(int, input().split())

arr = [i+1 for i in range(N)]

answer = "<"
idx = 0

while len(arr)>0:
    idx+=K
    idx-=1
    
    if idx>=len(arr):
        idx%=len(arr)
    answer += str(arr[idx])
    
    if len(arr)!=1:
        answer += ", "
        
    del arr[idx]
    
print(answer+">")