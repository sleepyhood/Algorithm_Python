import sys

input = sys.stdin.readline
print = sys.stdout.write

arr = input().rstrip()
arr = list(arr.split())

print(f"{len(arr)}\n")