import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = input().rstrip()
arr = list(map(int, arr.split()))

#order = [x for x in range(0, N+1)] #0~N

result = 0
for i in range(len(arr)):
    if arr[i] != i+1:
        result+=1

print(f"{result}\n")    