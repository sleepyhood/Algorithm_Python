import itertools
# 조합의 개수이므로.. 라이브러리만 알면 뚝딱일줄 알았다.
import math 
def solution(balls, share):
    answer = 0
    # b = [0]*balls
    # answer = len(list(itertools.combinations(b,share)))

    answer = math.factorial(balls) / (math.factorial(balls-share) * math.factorial(share))
    
    return answer