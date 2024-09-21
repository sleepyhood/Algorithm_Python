"""
[백준]
1755. 숫자놀이
https://www.acmicpc.net/problem/1755
"""
#첫째 줄에 M과 N이 주어진다.
m, n = map(int, input().split())

# 인덱스에 매칭되는 숫자 영문명
eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

li = []

# [영문명, 숫자] 형태로 매핑

for i in range(m, n+1):
    if i >= 10:
        tmp = ""
        for j in str(i):
            tmp+=eng[int(j)]
            tmp+=" "
        li.append([tmp, i])
    else:
        li.append([eng[i], i])

# 영문명을 기준으로 오름차순 정렬
li.sort()

# 주의: 한줄에 10개씩 출력
cnt = 1
for l, r in li:
    if cnt%10==0:
        print(r)
    else:
        print(r, end= " ")
    cnt+=1