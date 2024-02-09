import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())    

arr = [i for i in range(10000)]

for j in range(1, 10000):
    arr[j]+=arr[j-1]
    
while n!=-1:
    temp = [1]
    for i in range(2,n):
        if n%i==0:
            temp.append(i)
    if sum(temp) == n:
        print(f"{n} = ")
        for i in temp:
            print(f"{i}")
            if i == temp[-1]:
                print(f"\n")
                continue
            print(f" + ")
    else:
        print(f"{n} is NOT perfect.\n")      
    n = int(input().rstrip())            
