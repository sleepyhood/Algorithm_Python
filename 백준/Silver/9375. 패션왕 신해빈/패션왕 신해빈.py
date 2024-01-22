import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    _dict = {}
    for i in range(n):
        clothes, category = (input().rstrip()).split()
        if category not in _dict:
            _dict[category] = []
        _dict[category].append(clothes)
            
    cnt = 1
    for k in _dict:
        cnt *= (len(_dict[k])+1)
        # (옷을 입은 경우 + 안 입은 경우)
        
    print(f"{cnt-1}\n")        # 모든 옷을 안 입는 경우는 없으므로 1은 뺌