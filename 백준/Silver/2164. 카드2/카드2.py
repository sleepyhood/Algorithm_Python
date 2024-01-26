from collections import deque

N = int(input())

# 1234-> 234-> 342-> 42-> 24-> 4
# 123456-> 23456-> 
# 홀수는 버리고, 짝수번째는 아래로

l = [x for x in range(1, N+1)]
l = deque(l)

while len(l)>1:
    l.popleft()
    l.append(l.popleft())
print(l.popleft())
