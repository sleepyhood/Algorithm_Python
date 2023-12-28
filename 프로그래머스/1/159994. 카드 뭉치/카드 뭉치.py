def solution(cards1, cards2, goal):
    answer = ''
    c1,c2 = 0,0
    
    for i in range(len(goal)):
        if goal[i] == cards1[c1]:
            if c1+1< len(cards1):
                c1+=1
            
        elif goal[i] == cards2[c2]:
            if c2+1< len(cards2):
                c2+=1
        else:
            return 'No'
        
    return 'Yes'