import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

_list = map(int, (input().rstrip()).split())
_list = sorted(list(set(_list)))

for i in _list:
    print(f"{i} ")
