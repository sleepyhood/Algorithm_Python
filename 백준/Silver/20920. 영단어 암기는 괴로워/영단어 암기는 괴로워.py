from collections import defaultdict

n, m = map(int, input().split())

li = []
dic=defaultdict(lambda: [0, 0]) # value를 리스트로 가지는 법

for _ in range(n):
    word = input()
    if len(word) < m:
        continue

    dic[word][0]+=1
    dic[word][1] = len(word)

# value[1]의 빈도, 길이를 내림차순
#dic = sorted(dic.items())

dic = sorted(dic.items(), key=lambda x:(-x[1][0], -x[1][1], x[0]))
for key in dic:
    print(key[0])