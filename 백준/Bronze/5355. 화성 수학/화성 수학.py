T = int(input())

for _ in range(T):
    mars = list(input().split())
    result = float(mars[0])
    #print(f"{mars}\n")
    for i in range(1, len(mars)):
        if mars[i] == '@':
            result*=3
        elif mars[i] == '%':
            result+=5
        else:
            result-=7
    print(f"{result:.2f}")