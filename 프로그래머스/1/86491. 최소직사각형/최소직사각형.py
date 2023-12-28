def solution(sizes):
    for i in sizes:
        i.sort()
    sizes.sort()
    
    w, h = sizes[0][0], sizes[0][1]
    for s in sizes:
        if s[0]>w :
            w = s[0]
        if s[1]>h:
            h = s[1]
    return w*h