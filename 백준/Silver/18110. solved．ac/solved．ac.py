import sys

input = sys.stdin.readline

def my_round(num):

    lst = num - int(num)

    if lst >= 0.5 :
        return int(num)+1
    else:
        return int(num)


n = int(input().rstrip())

exclude = my_round(n*0.15)
li = []

for i in range(n):
    li.append(int(input().rstrip()))

li.sort()

# 합을 구할 구간: [exclude] ~ [n-exclude]

_sum = 0
for i in range(exclude, n-exclude):
    _sum+=li[i]

if n - exclude*2 > 0:
    print(my_round(_sum/(n - exclude*2)))
else:
    print(0)