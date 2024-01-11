grade = input()
result = 0

if grade=="F":
    result = 0.0
else:
    result = float(ord('A') - ord(grade[0]) + 4)
    if grade[1] == '+':
        result+=0.3
    elif grade[1] == '-':
        result-=0.3    
print(result)