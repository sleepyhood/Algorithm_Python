total = int(input())
n = int(input())
tempSum = 0

for i in range(n):
    money, mul = map(int, input().split())
    tempSum+= money*mul

if tempSum==total:
    print("Yes")
else:
    print("No")