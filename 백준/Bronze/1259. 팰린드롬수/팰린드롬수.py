import sys

input = sys.stdin.readline
print = sys.stdout.write

while True:
    n = input().rstrip()
    if n == '0':
        break
    isPalindrome = True
    for i in range(len(n)//2):
        if n[i] != n[(i+1)*-1]:
            isPalindrome = False
            break
    if isPalindrome:
        print("yes\n")
    else:
        print("no\n")