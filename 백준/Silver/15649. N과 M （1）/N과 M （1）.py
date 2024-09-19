#math라이브러리 사용
import math 


def sol (li, use):
    global m
    global n
    #global maxCnt
    #print(m)
    tmp = li[:]

    if len(li) == m:
        for e in tmp:
            print(e, end=" ")
        print()
        return

    for i in range(1, n+1):
        if use[i] == 1:      # 기존에 사용했던 원소라면, 넘기기
            continue
        use[i] = 1
        tmp.append(i)
        
        sol(tmp, use)

        tmp.pop()   # sol 함수를 호출할 때 append된 값 지우는 용도
        use[i] = 0  # sol 함수를 호출할 때 사용 체크된 값 초기화



n, m = map(int, input().split())
_list = []
used = [0]*9    # 1~8까지 사용 여부 확인

# n과 m(2)에서 추가
# 중복을 허용하지 않는 조합
# 각 숫자는 최대 (조합의 수) / (숫자의 종류)만큼 나올 수 있다.
#comb = math.factorial(n)// (math.factorial(n-m))
#maxCnt = comb // n

sol(_list, used)