from collections import deque
import sys
"""
123-4567-89
"""

import random
import re

input = sys.stdin.readline
print = sys.stdout.write

def generate_random_query(length):
    query = []
    last_was_hyphen = False  # 하이픈 연속 방지 플래그
    for _ in range(length):
        if random.choice([True, False]):  # True일 경우 숫자
            query.append(str(random.randint(1, 9)))
        else:  # False일 경우 하이픈
            query.append('-')
            last_was_hyphen = True

    # for _ in range(length):
    #     if last_was_hyphen:
    #         # 직전에 하이픈이 나왔다면 숫자를 추가
    #         query.append(str(random.randint(1, 9)))
    #         last_was_hyphen = False
    #     else:
    #         # 랜덤으로 숫자나 하이픈 중 하나를 선택
    #         if random.choice([True, False]):  # True일 경우 숫자
    #             query.append(str(random.randint(1, 9)))
    #         else:  # False일 경우 하이픈
    #             query.append('-')
    #             last_was_hyphen = True
    query[0]=(str(random.randint(1,9)))
    #query[-1]=(str(random.randint(1,9)))
    return ''.join(query)


def process_string(T):
    S = []  # 문자열을 리스트로 유지
    X = 0   # 초기 합
    #sys.set_int_max_str_digits(99999999)  
# Set a higher limit if needed
    for char in T:
        if char == '-':
            # 문자열 리스트를 역순으로 정렬하여 다시 합침
            S = S[::-1]
        else:
            # 숫자를 리스트에 추가
            S.append(char)
            # 리스트를 문자열로 변환하고, 정수로 변환 후 합산
            X += int(''.join(S))

    return X


# 예시: 길이 300의 랜덤 쿼리 생성
#leng = 100
#random_query = generate_random_query(leng)
#print(f"입력값: {random_query}\n")


#q = random_query
q = input().rstrip()
#q = "1234-567-89-123"
# 예시
#result=""
#result = process_string(q)
#print(f"문자열연산된 정답: {result}\n")  # 결과 출력

q = q.split('-')
"""
#WTF
if len(q)<2:
    print(str(q[0]))
    quit()
    """

lens = [len(e) for e in q]
#sumLens = prefixSum(lens)


oddCnt = sum(lens[::2])  # 반전된 짝수번째 인덱스가 나올 횟수
evenCnt = sum(lens[1::2])  # 반전된 홀수번째 인덱스가 나올 횟수


ans = [0]*(sum(lens))

"""
    홀수번째 정방향
"""
for i in range(0,len(q), 2):
    for j in range(len(q[i])):
        ans[-(oddCnt)] += int(q[i][j])
        #ans[-1]+=int(q[i][j])
        oddCnt-=1
#print(f"ans: {ans}\n")
"""
    짝수번째 정방향
"""
for i in range(1,len(q), 2):
    for j in range(len(q[i])):
        ans[-(evenCnt)] += int(q[i][j])
        #ans[-1]+=int(q[i][j])
        evenCnt-=1
#print(f"ans: {ans}\n")
evenReCnt = sum(lens[::2])  # 반전된 짝수번째 인덱스가 나올 횟수
oddReCnt = sum(lens[1::2])  # 반전된 홀수번째 인덱스가 나올 횟수


#print(f"evenReCnt: {evenReCnt}")
#print(f"oddReCnt: {oddReCnt}")
#ans2 = [0]*sum(lens)

odds = q[::2]
evens = q[1::2]
#print(odds)
#print(evens)

"""
    홀수번째 역방향
"""

# 홀수개수만큼 쿼리가 있다면, 마지막 쿼리는 역방향이 존재하지 않는다.
if len(q)%2!=0:
    odds.pop()

idx = oddReCnt          # 오른쪽 누적합 시작위치(양수) 
repeatCnt = oddReCnt    # 오른쪽 누적합 끝나는 위치(음수)


#print(f"{odds}\n")
for i in range(len(odds)):
    #print(f"{odds[i]}\n")
    #print(f"i: {i}\tevens: {evens[i]}\n")
    for j in odds[i]:
        # -(evenReCnt+idx)부터 evenReCnt만큼 반복
        #print(f"-(idx+1+1): {-(idx+1)}\n")
        #print(f"-(idx-repeatCnt): {-(idx-repeatCnt+1)}\n")
        ans[-(idx+1)] += int(j)
        ans[-(idx-repeatCnt+1)] -= int(j)
        idx+=1
    if i >= len(evens):
        continue
    repeatCnt -= int(len(evens[i]))
#print(f"ans: {ans}\n")


"""
    짝수번째 역방향
"""


evenReCnt = sum(lens[::2])  # 반전된 짝수번째 인덱스가 나올 횟수
oddReCnt = sum(lens[1::2])  # 반전된 홀수번째 인덱스가 나올 횟수


#print(f"evenReCnt: {evenReCnt}")
#print(f"oddReCnt: {oddReCnt}")
#ans2 = [0]*sum(lens)

odds = q[::2]
evens = q[1::2]



# 짝수개수만큼 쿼리가 있다면, 마지막 쿼리는 역방향이 존재하지 않는다.
if len(q)%2==0:
    evens.pop()
    
idx = evenReCnt                         # 오른쪽 누적합 시작위치(양수) 
repeatCnt = evenReCnt-int(len(odds[0]))  # 오른쪽 누적합 끝나는 위치(음수)
odds.pop(0)
# 짝수번째 항목들은, 첫번째쿼리의 길이에 영향을 받지 않는다.

for i in range(len(evens)):
    #print(f"{evens[i]}\n")
    #print(f"i: {i}\todds: {odds[i]}\n")
    for j in evens[i]:
        # -(evenReCnt+idx)부터 evenReCnt만큼 반복
        #print(f"-(idx+1): {-(idx+1+1)}\n")
        #print(f"-(idx+1-repeatCnt): {-(idx+2-repeatCnt)}\n")
        ans[-(idx+1)] += int(j)
        ans[-(idx-repeatCnt+1)] -= int(j)
        idx+=1
    if i >= len(odds):
        continue
    repeatCnt -= int(len(odds[i]))

#print(f"ans: {ans}\n")
# 오른쪽 방향으로 누적합 수행
# for i in range(len(ans)-2, -1, -1):
#     ans[i]+=ans[i+1]

# 왼쪽 방향으로 누적합 수행
for i in range(1, len(ans)):
     ans[i]+=ans[i-1]


# 오른쪽 방향으로 자리올림 수행
carry=0
for i in range(len(ans)-1, -1, -1):
    ans[i]+=carry
    carry=ans[i]//10
    ans[i]%=10

# 만약 자리올림이 남아있을 경우
if carry>0:
    ans=deque(ans)
    while carry>0:
        #print(f"carry: {carry}\n")
        ans.appendleft(carry%10)
        carry//=10
    #ans[0]+=carry
#print(f"bbb:{ans}")

ans = list(map(str, ans))
ans = ''.join(ans)
ans = ans.lstrip('0')

print(f"{ans}\n")

#print(f"\n{ans==str(result)}\n")

# if ans[0]!=0:
#     print(str(ans[0]))
    
# for i in range(1,len(ans)):
#     #print(str(ans[i]), end = "")
#     print(str(ans[i]))
    