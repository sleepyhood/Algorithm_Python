n = int(input())
q1, q2, q3, q4, axis = 0,0,0,0,0
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        axis+=1
    else:
        if x>0:
            if y>0:
                q1+=1
            else:
                q4+=1
        else:
            if y>0:
                q2+=1
            else:
                q3+=1

print(f"Q1: {q1}\nQ2: {q2}\nQ3: {q3}\nQ4: {q4}\nAXIS: {axis}\n")                