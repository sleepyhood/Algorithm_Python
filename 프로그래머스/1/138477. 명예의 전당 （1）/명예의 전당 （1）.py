def solution(k, score):
    answer = []
    temp = []

    for item in score:
        temp.append(item)
        temp.sort() 
        if len(temp)>k:
            if item>=temp[0]: # 새로운 최댓값 존재시
                del temp[0]
                
        answer.append(temp[0])

    return answer