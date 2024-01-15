import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
arr = []
_dict = {}

for _ in range(N):
    temp = input().rstrip()
    if temp not in _dict.keys():
        _dict[temp] = len(temp)
        
# 딕셔너리의 값을 길이가 짧은 것부터 기준으로 정렬
# 만약 길이가 같다면 사전순
sorted_by_key_and_value = sorted(_dict.items(), key=lambda x: (x[1], x[0]))

for key, value in sorted_by_key_and_value:
    print(f"{key}\n")