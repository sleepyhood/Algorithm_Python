N = int(input())

zero, one = 0, 0
for _ in range(N):
    inp = int(input())
    if inp == 1:
        one+=1
    else:
        zero+=1
if zero>one:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
