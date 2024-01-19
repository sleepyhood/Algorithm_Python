import sys
import math as m

input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, (input().rstrip().split()))
           
result = m.factorial(N) // (m.factorial(K) * m.factorial(N-K))
print(f"{result}\n")           