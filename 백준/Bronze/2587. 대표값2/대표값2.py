arr = []

for _ in range(5):
    temp = int(input())
    arr.append(temp)
    
arr.sort()

print(sum(arr)//5)
print(arr[2])