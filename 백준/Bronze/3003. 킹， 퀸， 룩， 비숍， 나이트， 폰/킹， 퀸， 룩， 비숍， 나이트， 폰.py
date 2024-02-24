arr = list(map(int, input().split()))

result = [0]*len(arr)

for i in range(len(arr)):
    if i< 2:
        result[i] = 1 - arr[i]
    elif i<5:
        result[i] = 2 - arr[i]
    else:
        result[i] = 8 - arr[i]

for i in result:
    print(i, end = " ")