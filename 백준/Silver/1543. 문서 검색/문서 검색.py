sen = input()
find = input()
cnt = 0

while find in sen:
    sen = sen.replace(find, "#", 1)
    cnt+=1
print(cnt)