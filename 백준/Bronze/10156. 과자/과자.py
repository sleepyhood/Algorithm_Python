K, N, M = map(int, input().split())
result = (K*N) - M
if result < 0: # 돈이 더 많은 경우
    result = 0
print(f"{result}\n")