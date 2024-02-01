def sol():
    import sys

    input = sys.stdin.readline
    print = sys.stdout.write

    N = int(input().rstrip())

    result = []

    for _ in range(N):
        _list = list(map(int, (input().rstrip()).split()))
        if len(set(_list)) == 1: # 모두 같은 케이스
            result.append(_list[0]*1000 + 10000)
        elif len(set(_list)) == 2: # 2개만 같음
            temp = list(set(_list))
            if _list.count(temp[0]) == 2: #2개인 항목이 0번지
                result.append(temp[0]*100 + 1000)
            else:
                result.append(temp[1]*100 + 1000)
        else:    # 모두 다름
            result.append(max(_list)*100)
            
    print(f"{max(result)}\n")    
sol()    