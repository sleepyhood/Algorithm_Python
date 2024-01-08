arr = list(map(int, input().split()))
resultArr = []

while sum(arr)!=0:
    arr.sort()
    result = ""
    # 삼각형이 아님
    if arr[0]+arr[1]<=arr[2]:
        result = "Invalid"
        
    # 세 변이 모두 동일
    elif len(set(arr)) == 1:
        result = "Equilateral"
        
    # 두 변이 같을 경우
    elif len(set(arr)) == 2:
        result = "Isosceles"
   
    # 세 변이 모두 다름
    else:
        result = "Scalene"
    resultArr.append(result)
    arr = list(map(int, input().split()))
    
for item in resultArr:
    print(item)
    