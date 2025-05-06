n = int(input())

str1 = input()

r = 31
m = 1234567891
res = 0

for i in range(n):
    char = ord(str1[i]) - ord('a') + 1
    res += char * (r)**(i) 
    res%=1234567891
print(res)