import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, (input().rstrip()).split())

numWiki = {}
nameWiki = {}

for i in range(N):
    temp = input().rstrip()
    numWiki[str(i+1)] = temp
    nameWiki[temp] = str(i+1)

for i in range(M):
    temp = input().rstrip()
    if temp in numWiki:
        print(f"{numWiki[temp]}\n")
    if temp in nameWiki:
        print(f"{nameWiki[temp]}\n")