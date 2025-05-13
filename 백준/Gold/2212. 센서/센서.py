n = int(input())
k = int(input())

li = list(map(int, input().split()))

li.sort()

dist = []

# 예왜 처리
# 집중국이 훨씬 많을 경우, 매 좌표마다 설치 가능 
if k >= n:
    print(0)
    exit()

for i in range(1, n):
    dist.append(li[i]-li[i-1])

dist.sort(reverse=True)
# 이전에 배운 외양간 판자 문제와 매우 유사하다!!
# 전체 길이 - (k-1 개의 가장 긴 판자)

total = li[-1] - li[0]

for i in range(k-1):
    total-=dist[i]
print(total)