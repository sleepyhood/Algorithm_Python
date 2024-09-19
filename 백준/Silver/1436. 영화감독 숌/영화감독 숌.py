n = int(input())

# n번째 666은?
temp = 666
cnt = 1

while cnt<n:
    temp+=1
    if '666' in str(temp):
        cnt+=1
print(temp)    