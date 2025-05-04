# 단위행렬을 이용한 연산

def matrix_mult(A, B):
    # 2x2 행렬 곱셈
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % 1000000007,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % 1000000007],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % 1000000007,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % 1000000007],
    ]

def matrix_power(matrix, n):
    # 분할정복 방식의 행렬 거듭제곱
    result = [[1, 0], [0, 1]]  # 단위 행렬
    while n > 0:
        if n % 2 == 1:
            result = matrix_mult(result, matrix)
            n -= 1
        else:
            matrix = matrix_mult(matrix, matrix)
            n //= 2
    return result

def fibonacci(n):
    if n == 0:
        return 0
    base = [[1, 1], [1, 0]]
    result = matrix_power(base, n-1)
    return result[0][0]  # 또는 result[1][0]

n = int(input())
print(fibonacci(n) % 1000000007)