# - -> + 순서에서 음수부호 앞에 괄호가 추가되어야 최소값

import sys
input = sys.stdin.readline
print = sys.stdout.write

expression = (input().rstrip()).split('-')   # -단위로 끊음 

# ['55', '50+40']
# ['10+20+30+40']

result = 0

for i in range(len(expression)):
    if '+' in expression[i]:
        expression[i] = expression[i].split('+')
        expression[i] = map(int, expression[i])
        expression[i] = sum(expression[i])
    else:
        expression[i] = int(expression[i])
    
    #print(f"{expression[i]}\n")

    if i == 0:
        result = expression[i]
        continue
    result-=expression[i]
print(f"{result}\n")    