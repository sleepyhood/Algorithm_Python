import sys

input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, (input().rstrip()).split())

print('<')

arr = [i for i in range(1, N+1)]
idx = K-1

while arr:
    print(f"{arr[idx]}")
    del arr[idx]
    idx += K-1
    if idx>=len(arr) and len(arr)>0:
        idx %= len(arr)
    if len(arr) == 0:
        print(f">\n")
    else:
        print(f", ")
