"""
[백준]
23046. 큰 수 뒤집기
https://www.acmicpc.net/problem/23046

최종 설명 및 요약본
- 불필요한 함수 및 주석 제거됨
"""

from collections import deque
import sys

import random
import re

input = sys.stdin.readline
print = sys.stdout.write

# 입력 테스트용 함수
def generate_random_query(length):
    query = []
    for _ in range(length):
        if random.choice([True, False]):  # True일 경우 숫자
            query.append(str(random.randint(1, 9)))
        else:  # False일 경우 하이픈
            query.append('-')


    query[0]=(str(random.randint(1,9)))
    return ''.join(query)

# 랜덤 쿼리 생성
#leng = 100
#random_query = generate_random_query(leng)
#print(f"입력값: {random_query}\n")


#q = random_query
q = input().rstrip()
q = q.split('-')

"""
# >>>>삽질의 주범<<<<
# 쿼리가 하이픈없이 하나만 있다면, 이는 원래의 값을 출력하란 의미가 아니다.
if len(q)<2:
    print(str(q[0]))
    quit()
 """

lens = [len(e) for e in q]  
# 각 쿼리의 길이를 저장하는 리스트
# 하이픈 한개만을 기준으로 잘린 길이이므로, 하이픈이 2개 이상일 경우 해당 개수-1개만큼 길이 0이 존재

ans = [0]*(sum(lens))
# 정답을 저장할 리스트

oddCnt = sum(lens[::2])  # 홀수번째 인덱스가 나올 횟수
evenCnt = sum(lens[1::2])  # 짝수번째 인덱스가 나올 횟수


# 아래부터는 숫자가 나올 위치를 미리 배치하는 코드
# 정방향은 최종적으로 나올 위치부터 [-1]번지까지 누적된다.
"""
    1. 홀수번째 정방향
"""
for i in range(0,len(q), 2):
    for j in range(len(q[i])):
        ans[-(oddCnt)] += int(q[i][j])
        #ans[-1]+=int(q[i][j])
        oddCnt-=1

"""
    2. 짝수번째 정방향
"""
for i in range(1,len(q), 2):
    for j in range(len(q[i])):
        ans[-(evenCnt)] += int(q[i][j])
        #ans[-1]+=int(q[i][j])
        evenCnt-=1




# 역방향은 최종적으로 나올 위치부터 구간합으로 누적된다.

evenReCnt = sum(lens[::2])  # 반전된 짝수번째 인덱스가 나올 횟수
oddReCnt = sum(lens[1::2])  # 반전된 홀수번째 인덱스가 나올 횟수

odds = q[::2]       # 홀수번쨰 인덱스에 있는 원소
evens = q[1::2]     # 짝수번쨰 인덱스에 있는 원소

"""
    3. 홀수번째 역방향
"""

idx = oddReCnt          # 누적합 시작위치
repeatCnt = oddReCnt    # 누적합 끝나는 위치

for i in range(len(odds)):
    for j in odds[i]:
        ans[-(idx+1)] += int(j)             # 새로 들어온 숫자는 기존 숫자로부터 1칸씩 밀려남
        ans[-(idx-repeatCnt+1)] -= int(j)   
        idx+=1
    if i >= len(evens):     # 짝수와 홀수는 길이가 다를 수밖에 없으므로 먼저 확인
        break
    repeatCnt -= int(len(evens[i]))         # 반복횟수는 짝수번째 행의 길이에 영향을 끼친다.



"""
    4. 짝수번째 역방향
"""


# 짝수개수만큼 쿼리가 있다면, 마지막 쿼리는 역방향이 존재하지 않는다.
if len(q)%2==0:
    evens.pop()
    
idx = evenReCnt                         # 누적합 시작위치 
repeatCnt = evenReCnt-int(len(odds[0]))  # 누적합 끝나는 위치
odds.pop(0)

# 짝수번째 항목들은, 첫번째쿼리의 길이에 영향을 받지 않는다.

for i in range(len(evens)):
    for j in evens[i]:
        ans[-(idx+1)] += int(j)
        ans[-(idx-repeatCnt+1)] -= int(j)
        idx+=1
    if i >= len(odds):
        break
    repeatCnt -= int(len(odds[i]))


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
    ans.appendleft(carry%10)


# 최종 출력
# 정수 리스트를 문자열 리스트로 변환 후, 통째로 문자열로 변환
ans = list(map(str, ans))
ans = ''.join(ans)
ans = ans.lstrip('0')

print(f"{ans}\n")
    