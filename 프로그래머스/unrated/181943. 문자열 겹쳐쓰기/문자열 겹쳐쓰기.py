def solution(my_string, overwrite_string, s):
    answer = ''
    idx = 0
    while idx<len(my_string):
        if idx == s:
            ovIdx = 0
            while ovIdx < len(overwrite_string):
                answer+=overwrite_string[ovIdx]              
                ovIdx+=1
            idx +=len(overwrite_string)
            idx-=1
        else:
            answer+=my_string[idx]
        idx+=1
    return answer