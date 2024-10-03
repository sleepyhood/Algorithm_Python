"""
[백준]
25328. 문자열 집합 조합하기
https://www.acmicpc.net/problem/25328
"""

import heapq
import sys
import math
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

"""
[백트래킹]

알파벳 소문자로 구성된 문자열 X, Y, Z가 주어진다. 
각각의 문자열에는 중복된 문자가 존재하지 않는다. 
문자열 S에 있는 문자 중 임의로 k개를 선택하여 문자열 S에서의 순서를 유지하여 만든 모든 부분 문자열을 모아 놓은 집합을 문자열 S에 대한 조합 C(S, k)라고 하자. 
예를 들어, 문자열 S = 'abc'에 대한 조합 C(S, 2) = {'ab', 'ac', 'bc'}이다. 
입력으로 문자열 X, Y, Z와 정수 k가 주어질 때 C(X, k), C(Y, k), C(Z, k)에 두 번 이상 나타나는 부분 문자열을 오름차순으로 출력하자.
"""

def sol(st, tmp, k, idx):
    global res
    if k == 0:  # 반복횟수 최대인 경우
        res.append(tmp)
        return
    for i in range(idx, len(st)):
        sol(st, tmp+st[i], k-1, idx+1)
        idx+=1

# 입력    
#t = int(input())
#x, y = map(int, input().split())

s1 = input()
s2 = input()
s3 = input()
k = int(input())


tmp = ""
res = []
sol(s1, tmp, k, 0)
sol(s2, tmp, k, 0)
sol(s3, tmp, k, 0)

# 2개 이상 출현한 문자만 사용
_dict = {}
ans = set()

for e in res:
    if e in _dict:
        _dict[e]+=1
        ans.add(e)
    else:
        _dict[e] = 1


if len(ans) == 0:
    # 만약 모든 문자가 2개 미만 사용시 정답은 -1
    print(-1)

else:
    ans = sorted(list(ans))
    for e in ans:
        print(e)