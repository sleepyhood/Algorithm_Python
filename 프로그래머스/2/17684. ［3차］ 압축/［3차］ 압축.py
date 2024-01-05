# A의 아스키 코드는 65
def solution(msg):
    answer = []
    my_alpha = ['']*27
    
    listLen = 1
    for i in range(1, 27):
        my_alpha[i] = chr(65+i-1)
        listLen +=1
        
    scope = 0
    idx = 0
    
#   반복시 고려할 것:
#   1. 뒤에 있는거 까지 묶어도 my_alpha에 존재하는가?
#       1-1. 존재할 경우:
#           존재하지 않을 때까지 반복 확인, 존재하는 것까지만 인덱스 이동
#       1-2. 존재하지 않을 경우:
#           새로 묶어서 my_alpha에 저장, 존재하는 것까지만 인덱스 이동

    while idx<len(msg)-1:
        st = msg[idx]
        now = idx
        # print(f"idx: {idx}", end = " ")
#       반복 종료조건: 묶었을 때 my_alpha에 없을 경우(신규 단어)
#       신규 단어 유무에 관계없이 인덱스는 이동해야함
        while st in my_alpha and idx+1<len(msg):
            idx+=1
            st+=msg[idx]
        # print(f"idx: {idx}", end = " ")
        # idx-=1        
        if idx == len(msg)-1:
            if st[:len(st)] in my_alpha:
                answer.append(my_alpha.index(st[:len(st)]))
                idx-=1
                break
            # else:
            #     answer.append(my_alpha.index(msg[idx]))
            #     break
            
        my_alpha.append(st[:len(st)])
        
        
            
        answer.append(my_alpha.index(st[:len(st)-1]))
        
        tempIdx = 0
        
        if len(st[:len(st)])>2:
            tempIdx = len(st[:len(st)-1])-1
        idx=now+1+tempIdx
        # print(f"idx: {idx}")

        # print(f"st[:len(st)]: {st[:len(st)]:^5} + {my_alpha.index(st[:len(st)])} , st[:len(st)-1]: {st[:len(st)-1]:^5} + {my_alpha.index(st[:len(st)-1])}")
        # print("")
        
    # if idx-1<len(msg):
    #     answer.append(my_alpha.index(msg[idx-1:]))
    print(f"idx: {idx}", end = " ")
    if idx == len(msg)-1:
        answer.append(my_alpha.index(msg[idx]))
    return answer     