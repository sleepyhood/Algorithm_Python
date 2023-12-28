def solution(n, m, section):
    answer = 0
    check = [1] * (n+1)

    for i in section:
        check[i] = 0 
        
    i = 1
    while i<=n:
        if check[i] == 0:
            answer+=1
            end = i+m-1
            if(end>n):
                end = n
            for j in range(i, end+1):
                check[j]=1
        i+=1
        #print(check)  
            
            
    return answer