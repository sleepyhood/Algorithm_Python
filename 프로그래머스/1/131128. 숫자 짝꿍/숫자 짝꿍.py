def solution(X, Y):
    answer = ''
    lx = [0 for i in range(10)]
    ly = [0 for i in range(10)]
    tmp = [0 for i in range(10)]
    arr = []
    for i in X:
        lx[int(i)]+=1
    for i in Y:
        ly[int(i)]+=1
        
    for i in range(10):
        if lx[i]>0 and ly[i]>0:
            tmp[i] = min(lx[i], ly[i])
            for j in range(tmp[i]):
                arr.append(i)
                
    arr.sort(reverse = True)

    if sum(arr)==0 and len(arr)!=0:
        answer = '0'
    elif arr:   # 원소가 존재할 경우
        for i in arr:
            answer+=str(i)
    else:       # 원소가 없을 경우
        answer = '-1'
    return answer