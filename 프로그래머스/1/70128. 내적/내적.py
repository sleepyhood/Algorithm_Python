import numpy as np
def solution(a, b):
    a = np.array(a, dtype = int)
    b = np.array(b)
    answer = a * b
    answer=list([int(x) for x in answer])
    # 내부 원소를 int64가 아닌 int로 바꿔줘야 인지
    print(sum((answer)))
    return sum(list(answer))