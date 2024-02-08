import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())

for _ in range(T):
    Yonsei = 0
    Korea = 0
    
    for _ in range(9):
        y, k = map(int, (input().rstrip()).split())

        Yonsei+=y
        Korea+=k
    
    if Yonsei > Korea:
        print(f"Yonsei\n")        
    elif Yonsei < Korea:        
        print(f"Korea\n")
    else:
        print(f"Draw\n")
    