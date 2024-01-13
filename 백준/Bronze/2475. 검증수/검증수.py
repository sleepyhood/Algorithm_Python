import sys

input = sys.stdin.readline
print = sys.stdout.write

arr = input().rstrip()
arr = list(map(int, arr.split()))

result = 0
for i in arr:
    result += i*i
    
print(f"{result%10}\n")