import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, (input().rstrip()).split())

notListen = set([])
notSee = set([])

for _ in range(N):
    temp = input().rstrip()
    notListen.add(temp)
    
for _ in range(M):
    temp = input().rstrip()
    notSee.add(temp)

# 결과는 사전순 정렬    
result = list(notListen.intersection(notSee))
result.sort()

print(f"{len(result)}\n")
for name in result:
    print(f"{name}\n")