# math 모듈 import
import math

A, I = map(int, input().split())
N = I*A
while math.ceil(N/A)==I:
    N-=1
print(N+1)   
# N / A  = I