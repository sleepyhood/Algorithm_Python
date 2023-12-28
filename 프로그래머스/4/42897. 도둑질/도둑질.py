def solution(money):
    answer = 0
    length = len(money)

    d = [0] * length
    d2 = [0] * length
    d3 = [0] * length

    d[0] = money[0]
    d2[0] = 0
    d3[0] = 0

    d[1] = money[0]
    d2[1] = money[1]
    d3[1] = 0

    for i in range(2, length - 1):
        d[i] = max(d[i - 1], d[i - 2] + money[i])

    for i in range(2, length):
        d2[i] = max(d2[i - 1], d2[i - 2] + money[i])

    for i in range(2, length):
        d3[i] = max(d3[i - 1], d3[i - 2] + money[i])

    if d2[-1] == d3[-1] + money[-1]:
        answer = d3[-1]
    else:
        answer = max(d[-2], d2[-1])

    return answer
