def solution(ingredient):
    answer = 0
    temp = []
    hamburger = [1,2,3,1]
    for item in ingredient:
        temp.append(item)
        if len(temp) >=4:
            if temp[-1] == 1 and temp[-2] == 3 and temp[-3] == 2 and temp[-4] == 1:
                answer+=1
                for _ in range(4):
                    temp.pop()
    return answer