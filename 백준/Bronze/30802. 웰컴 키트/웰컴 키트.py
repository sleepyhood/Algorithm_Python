import math
n = int(input())
li = list(map(int, input().split()))
shirts, pens = map(int, input().split())

shirtBundle = 0

for i in li:
    if i==0:
        continue
    if i>shirts:
        shirtBundle+=math.ceil(i/shirts)
        continue
    shirtBundle+=1

print(f"{shirtBundle}")    
print(f"{n//pens} {n%pens}")