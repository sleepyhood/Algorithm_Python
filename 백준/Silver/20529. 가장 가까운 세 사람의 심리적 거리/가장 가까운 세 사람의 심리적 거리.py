import sys
from itertools import combinations

input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())#총 인원
    arr = list((input().rstrip()).split())
    
    #mbtis = set(arr)
    if len(arr)>32 :
        print(f"{0}\n")
        continue
    
    mbtis = list(set(combinations(arr, 3)))     # 3명의 학생씩 조합짜기

        
    #print(f"{comb}\n")
    result = 16    # 3명의 mbti가 모두 다르다고 가정
    for mbti in mbtis:    # 조합 중에서
        temp = 0
        # 집적화를 사용하여, 각 3명씩 지어진 mbti의 다른 글자개수를 합함
        temp += sum(c1 != c2 for c1, c2 in zip(mbti[0], mbti[1]))
        temp += sum(c1 != c2 for c1, c2 in zip(mbti[0], mbti[2]))
        temp += sum(c1 != c2 for c1, c2 in zip(mbti[1], mbti[2]))
        if temp==0:
            result = 0
            break
        elif temp < result:
            result = temp
    print(f"{result}\n")                
