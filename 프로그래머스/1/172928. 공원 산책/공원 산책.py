import numpy as np
def solution(park, routes):
    npArr = []
    for i in park:
        npArr.append(list(i))
    npArr = np.array(npArr)
    
    answer = []
    x, y = 0,0
    ex, ey = len(park[0])-1,len(park)-1     # 인덱스 기준
    
    for i in range(len(park)):
        if 'S' in park[i]:  # 시작위치 구하기
            y=i
            x=park[i].index('S')
            break

    for inst in routes:
        arr = inst.split(' ')
        arr[1] = int(arr[1])
        # 지나가는 길에 X가 한개라도 포함되지 않아야 한다.
        if arr[0]=='E' and x+arr[1]<=ex and 'X' not in npArr[y,x:x+arr[1]+1 ]:
            x+=arr[1]
        elif arr[0]=='W' and x-arr[1]>=0 and 'X' not in npArr[y,x-arr[1]:x+1]:
            x-=arr[1]
        elif arr[0]=='S' and y+arr[1]<=ey and 'X' not in npArr[y:y+arr[1]+1,x]:
            y+=arr[1]
        elif arr[0]=='N' and y-arr[1]>=0 and 'X' not in npArr[y-arr[1]:y+1,x]:
            y-=arr[1]
    
    answer.append(y)
    answer.append(x)
    return answer