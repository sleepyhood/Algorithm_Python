n, T = map(int, input().split())

boxes = [0] * (n+1)

for _ in range(T):
    i, j, k = map(int, input().split())
    boxes[i:j+1] = [k] * (j - i + 1)
    
for i in range(1, n+1):
    print(f"{boxes[i]}", end = " ")