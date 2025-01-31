# 대표적인 재귀 문제
# 기둥의 개수는 3개
# n개의 원반을 1->3으로 옮겨야함(단, 원판의 순서는 큰게 아래로)

# initial condition: 
result = []
def hanoi(n, left, middle, right):
    # global answer
    
    if n == 1:
        result.append([left, right])
        # print(f"!Move disk 1 from {left} to {right}")
        return
    
    hanoi(n - 1, left, right, middle)     # Step 1: 작은 원판들을 보조 기둥으로 이동
    result.append([left, right])
    # print(f"Move disk {n} from {left} to {right}")  # Step 2: 가장 큰 원판을 목적지로 이동
    hanoi(n - 1, middle, left, right)  # Step 3: 보조 기둥에 있는 원판들을 목적지로 이동

    
    #hanoi(n-1, )
    
    return result

def solution(n):
    # answer = [[]]
    
    answer = hanoi(n, 1, 2, 3)
    # answer.append(1)
    # print(answer)
    return answer