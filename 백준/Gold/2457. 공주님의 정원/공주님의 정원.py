

n = int(input())

flowers = []

for _ in range(n):
    sm, sd, em, ed = list(map(int, input().split()))
    # MMDD 형식으로 저장
    s = sm*100 + sd
    e = em*100 + ed
    flowers.append([s,e])

flowers = sorted(flowers, key=lambda x : (x[0], x[1]))

# for e in flowers:
#     print(e)
# print()


idx = 0
current = 301   # 3월 1일
end_date = 1201 # 12월 1일
cnt = 0
max_end = 0


while current < end_date:
    update = False

    while idx < n and flowers[idx][0] <= current:   
        # 현재 날짜(current) 이전에 피는 꽃들 중에서
        # 가장 늦게 지는 꽃을 찾는다.
        # 이 구간에서 가장 오래 피는 꽃을 선택해야 공백 없이 이어갈 수 있다.
        if flowers[idx][1] > max_end:   # 현재 꽃이 더 늦게 진다면
            update = True
            max_end = flowers[idx][1]
        # print(flowers[idx][0])
        idx+=1

    if not update:
        print(0)
        exit()

    current = max_end
    cnt+=1

print(cnt)