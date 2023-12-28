def solution(n):
    answer = 0
    for i in range(2, n):
        if n % i == 1:
            answer = i
            # 최소값이므로 구하면 바로 루프 탈출
            break
    return answer

# 예제 사용
result = solution(10)
print(result)
