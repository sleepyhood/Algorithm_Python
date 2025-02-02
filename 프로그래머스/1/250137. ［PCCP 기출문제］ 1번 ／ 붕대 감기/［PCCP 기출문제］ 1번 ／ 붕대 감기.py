def solution(bandage, health, attacks):
    answer = health
    times = 0
    helcnt = 0
    attIdx = 0
    survive = True
    
    while attIdx < len(attacks):
        if answer < 0:
            survive = False
            break
        
        if times == attacks[attIdx][0]: # 피격당하는 타이밍이라면
            answer-= attacks[attIdx][1]
            attIdx+=1
            helcnt = 0  # 연속치료 실패
        
        else:
            helcnt+=1   # 성공횟수부터 먼저 올라간다.

            if helcnt == bandage[0]:    # 연속 치료 성공시
                if answer + bandage[1] + bandage[2] > health:
                    answer = health
                else:                    
                    answer+= (bandage[1] + bandage[2] )
                helcnt = 0
            else:
                if answer + bandage[1] > health:
                    answer = health
                else:                    
                    answer+=bandage[1]

            
        times+=1
    
        #print(answer)
    if answer <= 0:
        answer = -1
    return answer