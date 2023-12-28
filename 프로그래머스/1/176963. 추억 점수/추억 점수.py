def solution(name, yearning, photo):
    answer = []
    for group in photo:
        yearSum = 0
        for i in range(len(name)):
            if name[i] in group:
                yearSum+=yearning[i]
        answer.append(yearSum)
    return answer