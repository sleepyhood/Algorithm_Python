n = int(input())

stack = []
poster = 0

for _ in range(n):
    w, h = map(int, input().split())
    
    while len(stack) > 0 and stack[-1] > h:
        stack.pop()
        
    if len(stack) > 0 and stack[-1] == h:
        continue

    stack.append(h)
    poster+=1
    
    #print(stack)

print(poster)