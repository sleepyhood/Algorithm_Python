def solution(s):
    answer = [-1]*len(s)
    tmp = ['0']*len(s)
    for i in range(len(s)):
        if s[i] not in tmp:
            answer[i]= -1
        else:
            for j in range(i, -1, -1):
                if s[i] == tmp[j]:
                    answer[i]= i - j
                    break
        tmp[i] = s[i]
    return answer