def sol():
    # 전형적인 그리디 문제
    # 회의실을 자주 쓰려면, 한 타임당 적게 쓰는 쪽을 우선으로
    # 즉, 회의가 빨리 끝나는 쪽으로 오름차순
    import sys

    input = sys.stdin.readline
    print = sys.stdout.write

    N  = int(input().rstrip())

    _list = []

    for _ in range(N):
        start, end = map(int, (input().rstrip()).split())
        during = end - start
        _list.append([start, end])
        
    _list = sorted(_list, key = lambda x: (x[1], x[0]) )    # 마감시간, 시작시간 오름차순

    #print(f"{_list}\n")
    endTime = 0
    cnt = 0
    for s,e in _list:
        if s >= endTime:    # 회의시작시간이 마지막 사용시간 이후인 경우(또는 곧바로 회의)
            cnt+=1
            endTime = e
    print(f"{cnt}\n")
    
sol()    