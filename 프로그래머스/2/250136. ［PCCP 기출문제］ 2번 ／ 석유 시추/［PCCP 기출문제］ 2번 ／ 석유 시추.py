import sys
sys.setrecursionlimit(1000000)    # 삽질의 원인1

# 1. DFS로 석유 면적 구하기
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(row, col, land, visited, num):
    
    visited[row][col] = num
    size=1    
    
    for k in range(4):
        nr = row + dr[k]
        nc = col + dc[k]
        
        if nr < 0 or nc < 0 or nr>= len(land) or nc>=len(land[0]):
            continue
        
        if land[nr][nc] == 0 or visited[nr][nc] != 0:
            continue
        
        size+=dfs(nr, nc, land, visited, num)
    
    return size

def solution(land):
    answer = 0
    visited = [[0 for j in range(len(land[0]))] for i in range(len(land))]
    num = 1
    sizes = {}  # 번호별 면적
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and visited[i][j] == 0:            
                sizes[num] = dfs(i, j, land, visited, num)
                
                num+=1
    #print(sizes)      
    
    # 2. 열별로 방문했던 곳을 set으로 묶기
    result = []
    for j in range(len(land[0])):
        s = set()
        for i in range(len(land)):
            if visited[i][j]!=0:
                s.add(visited[i][j])
        
        if len(s) > 0:  
            result.append(list(s))
        
    # 3. 각 열의 합 중 최대값 찾기
    for e in result:
        tmp = 0
        for ee in e:
            tmp += sizes.get(ee, 0)
        answer = max(answer, tmp)            
    # print(result)
    return answer