n = int(input())
li = [0]*n

for i in range(n):
    li[i] = int(input())



# 양수는 양수와, 음수는 음수와 묶기
# 이 때, 음수는 가장 작은 곳부터, 양수는 가장 큰 곳부터 출발
li.sort()

minus = []
plus = []
# 음수 분리
for e in li:
    if e > 0:
        break
    minus.append(e)

li.reverse()
# 양수 분리
# 이 때, 1은 제외
for e in li:
    if e <= 1:
        break
    plus.append(e)

plus_tmp = 0
minus_tmp = 0

# 양수 처리
for i in range(0, len(plus)-1, 2):
    plus_tmp+= (plus[i]*plus[i+1])
    
if len(plus)%2!=0:
    plus_tmp+=plus[-1]


# 반례: 
# 2
# 0 -1
# 이 때는 곱해야한다.
# 음수 처리
for i in range(0, len(minus)-1, 2):
    minus_tmp+= (minus[i]*minus[i+1])
    
if len(minus)%2!=0:
    minus_tmp+=minus[-1]


one_tmp = 0

for e in li:
    if e == 1:
        one_tmp+=1

print(plus_tmp+minus_tmp+one_tmp)