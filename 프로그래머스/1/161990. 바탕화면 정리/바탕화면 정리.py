def solution(wallpaper):
    answer = []
    lx, ly, rx, ry = len(wallpaper[0]),len(wallpaper), 0, 0
    
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x] == '#':
                if ly > y:
                    ly = y
                if lx > x:
                    lx = x
                    
                if ry < y:
                    ry = y
                if rx < x:
                    rx = x
    answer.extend([ly, lx, ry+1, rx+1])
    return answer