n = int(input())
# list로 안 바꿔서 삽질;;;
scores = list(map(int, input().split()))

maxScore = max(scores)
result = 0

for score in scores:
    result+=round(score/maxScore* 100, 3) 
    
result = round(result/n, 3)
print(result)
