n = int(input())

li = []
alpha ={}
for _ in range(n):
    tmp = input()
    li.append(tmp)

    digit = 1
    for i in range(len(list(tmp))-1, -1, -1):
        if tmp[i] not in alpha:
            alpha[tmp[i]] = digit
        else:
            alpha[tmp[i]]+= digit
        digit*=10

# 왼쪽 자리 일수록 9에 가까워야 한다.
# ACDEB
#   GCF
# A = 9
# C = 8
# 자리수마다 10배 하기

alpha = sorted(alpha.items(), key=lambda x: x[1], reverse=True)
alpha = dict(alpha)
num = 9
for key in alpha:
    alpha[key] = num
    num-=1

result = 0

for i in range(n):
    tmp = 0
    digit = 1

    for j in range(len(li[i])-1, -1, -1):
        key = li[i][j]
        tmp += (alpha[key])*digit
        digit*=10

    result+=tmp
print(result)