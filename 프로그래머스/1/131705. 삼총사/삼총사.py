
from itertools import combinations

def solution(number):
    number = list(combinations(number, 3))
    answer = 0
    for item in number:
        if sum(item)==0:
            answer+=1
    return answer