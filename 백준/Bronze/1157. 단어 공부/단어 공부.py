import sys

input = sys.stdin.readline
print = sys.stdout.write

arr = str(input().rstrip())
arr = arr.upper()
#arr = list(arr.split())

wordDict = {}

for i in arr:
    if i in wordDict.keys():
        wordDict[i]+=1
    else:
        wordDict[i]=1

# 최대값 찾기
max_value = max(wordDict.values())
    
result = []    
# 최대값을 가진 키 찾기
for key, value in wordDict.items():
    if value == max_value:
        result.append(key)
        
# 결과 출력
if len(result) == 1:
    print(f"{result[0]}\n")
else:
    print(f"?\n")