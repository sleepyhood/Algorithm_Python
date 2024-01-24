import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
ioi = ''
# N은 0의 개수, N+1개의 1의 개수와 이루어짐

for i in range(N+N+1):
    if i%2!=0:
        ioi += 'O'
    else:
        ioi += 'I'       
        
M = int(input().rstrip())
S = input().rstrip()    

cnt = 0
idx = 0

while idx<M and ioi in S:
    left = S.index(ioi) # 글자가 나오는 시점
    idx = left+len(ioi)-1
    cnt+=1
    
    S = list(S)
    S[left] = '#'    # 중복되어서 판별해야 하므로 확인한 지점만 체크
    S = ''.join(S) # list를 공백없이 str로 만듦


print(f"{cnt}\n")


