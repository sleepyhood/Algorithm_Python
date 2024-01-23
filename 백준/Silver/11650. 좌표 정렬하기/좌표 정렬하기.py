import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
arr = []

for _ in range(N):
    x, y = map(int, (input().rstrip()).split())
    arr.append([x, y])

sorted_arr = sorted(arr, key=lambda x: (x[0], x[1]))
    
for i in range(N):
    print(f"{sorted_arr[i][0]} {sorted_arr[i][1]}\n")