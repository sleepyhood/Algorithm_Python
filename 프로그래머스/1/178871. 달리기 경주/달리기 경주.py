def solution(players, callings):
    answer = []
    
    dic = {}    # player가 key 
    
    rank = 1
    for i in players:
        dic[i] = rank
        rank+=1
    
    rank_dict= dict(map(reversed,dic.items()))  # rank가 key

    for i in range(len(callings)):
        # idx = players.index(callings[i]) # 해설진이 부른 플레이어
        # dic.get(callings[i])    # 딕셔너리 내부에 해당되는 값(순위) 출력
        
        currentRank = dic[callings[i]]          # 불린 플레이어의 랭크
        frontPlayer = rank_dict[currentRank-1]  # 앞 플레이어 이름
        # currentRank-1
        dic[callings[i]]-=1
        dic[frontPlayer]+=1
        
        rank_dict[currentRank-1] = callings[i]
        rank_dict[currentRank] = frontPlayer

    # print(dic)
    sorted_dict = sorted(dic.items(), key = lambda item: item[1])
    # print(sorted_dict)
    
    for i,j in sorted_dict:
        answer.append(i)
    
    return answer