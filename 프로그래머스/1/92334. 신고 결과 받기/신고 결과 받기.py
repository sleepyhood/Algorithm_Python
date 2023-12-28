def solution(id_list, report, k):
    answer = []
    
    report = list(set(report))
    reportedDict = dict.fromkeys(id_list,0)
    #reportedDict은 신고 "당한" 횟수를 저장
    for ch in report:
        tmp = ch.split()
        reportedDict[tmp[1]] += 1
    
    result = dict.fromkeys(id_list,0)
    
    for ch in report:
        tmp = ch.split()
        if reportedDict[tmp[1]] >=k:    # tmp[1]은 신고당한 사람
            result[tmp[0]] +=1          
            # 신고한 사람들의 메일 수 증가
    
    answer = list(result.values())
    
    return answer