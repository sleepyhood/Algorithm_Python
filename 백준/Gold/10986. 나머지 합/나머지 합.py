from collections import defaultdict

n, m = map(int, input().split())

li = list(map(int, input().split()))

ps = 0
# 어떤 두 인덱스 𝑖<𝑗에 대해 ps[j] - ps[i]가 m으로 나누어 떨어지려면
# ps[j] % m == ps[i] % m 이어야 함.
mod_count = defaultdict(int)
mod_count[0] = 1
cnt = 0

for num in li:
    ps += num
    mod = ps % m
    cnt += mod_count[mod]
    mod_count[mod] += 1

print(cnt)