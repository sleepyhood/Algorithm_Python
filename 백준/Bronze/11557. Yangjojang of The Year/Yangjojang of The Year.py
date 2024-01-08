T = int(input())
result = []
for _ in range(T):
    N = int(input())
    tempMax = 0
    tempSchool = ""
    for _ in range(N):
        S, L = input().split()
        L = int(L)
        if L>tempMax:
            tempSchool = S
            tempMax = L
    result.append(tempSchool)
        
        
        
for item in result:
    print(item)