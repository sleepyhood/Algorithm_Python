li = list(map(int, input().split()))

li.sort()

if li[0] + li[1] > li[2] or li[0] == li[1] == li[2]:
    print(sum(li))
else:
    while li[0] + li[1] < li[2]:
        li[2]-=1
    print(sum(li)-1)


