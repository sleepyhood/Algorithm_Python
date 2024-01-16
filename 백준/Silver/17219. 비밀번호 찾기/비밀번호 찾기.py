import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = (input().rstrip()).split()
N, M = int(N), int(M)

_dict = {}
for _ in range(N):
    site, password = (input().rstrip()).split()
    _dict[site] = password

for _ in range(M):
    site = input().rstrip()
    print(f"{_dict[site]}\n")