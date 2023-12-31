def solution(n, lost, reserve):
    answer = 0
    students = list(range(1, n+1))
    students = [1 for x in students]
    
    for i in lost:
        students[i-1]-=1
    
    for i in reserve:
        students[i-1]+=1
    
    for i in range(0, n-1):
        if students[i+1] >=2 and students[i] < 1:
            students[i+1] -=1
            students[i] +=1
            
        elif students[i+1] <1 and students[i] >=2:
            students[i+1] +=1
            students[i] -=1
            
    for i in students:
        if i>=1:
            answer+=1
            
    return answer