import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())

for _ in range(T):
    S = input().rstrip()
    R, S = S.split()
    R = int(R)
    
    for i in S:
        print(f"{i*R}")
    print("\n")

#print(f"{S[i-1]}\n")