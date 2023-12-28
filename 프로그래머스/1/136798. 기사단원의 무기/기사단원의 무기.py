# 1부터 n까지 약수를 셀 필요가 없다. => limit를 초과하는지가 핵심
# n**1/2까지만 반복 + 제곱수가 아니라면 약수는 항상 2개씩 쌍을 이룸
def cntdiv(n, limit):  # 약수를 세는 함수
    a = 1
    cnt = 0
    while a<int(n**(1/2))+1:
        if n%a ==0:
            if n**(1/2)==float(a):
                cnt+=1
                print("!")
            else:
                cnt+=2
                #n//=2
        # print(f"n: {n:^5} | cnt: {cnt:^5}")
        if cnt> limit:
            return -1
        a+=1
    return cnt

def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        result = cntdiv(i, limit)
        if result == -1:
            answer+=power
        else:
            answer+=result
        
    return answer