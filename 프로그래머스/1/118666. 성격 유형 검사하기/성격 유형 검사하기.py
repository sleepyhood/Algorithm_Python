def solution(survey, choices):
    answer = ''
    ind = {'R': 0, 'T':0, 'C':0, 'F':0, 'J': 0, 'M':0, 'A':0, 'N':0 }
    
    for i in range(len(survey)):
        if choices[i]>=5:
            ind[survey[i][1]] += choices[i] % 4
        elif choices[i]==3: 
            ind[survey[i][0]] += (choices[i]) - 2
        elif choices[i]==2: 
            ind[survey[i][0]] += (choices[i])
        elif choices[i]==1: 
            ind[survey[i][0]] += (choices[i]) + 2
            
    print(ind.items())
    
    if(ind['R']>=ind['T']):
        answer+='R'
    else:
        answer+='T'
        
    if ind['C']>=ind['F']:
        answer+='C'
    else:
        answer+='F'
        
    if ind['J']>=ind['M']:
        answer+='J'
    else:
        answer+='M'
     
    if ind['A']>=ind['N']:
        answer+='A'
    else:
        answer+='N'
        
    return answer