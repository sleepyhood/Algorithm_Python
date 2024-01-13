N = int(input())
row = N
col = 2

arr = [[0 for j in range(col)] for i in range(row)]

for i in range(N):
    x, y = map(int, input().split())
    arr[i][0] = x
    arr[i][1] = y
    
sorted_list = sorted(arr, key=lambda x: (x[1], x[0]))

for i in range(N):
    print(f"{sorted_list[i][0]} {sorted_list[i][1]}")
