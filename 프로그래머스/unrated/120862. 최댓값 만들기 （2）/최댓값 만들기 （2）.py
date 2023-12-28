def solution(numbers):
    l = sorted(numbers)
    print(l)
    minusCnt = 0;
    for i in l:
        if i<0:
            minusCnt+=1;

    if l[0]*l[1] > l[-1]*l[-2]:
        return l[0]*l[1]
    else:
        return l[-1]*l[-2]