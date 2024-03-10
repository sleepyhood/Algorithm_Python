T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    if A<B:
        A, B = B, A
    n1, n2 = A, B
    while n1%n2 != 0:
        tmp = n1%n2
        n1 = n2
        n2 = tmp   
    print(f"{A*B//n2}")        