"""

10 15
5 1 3 5 10 7 4 9 2 8

"""
n, s = map(int,input().split())
li = list(map(int,input().split()))

pli = [0 for i in range(n)]
pli[0] = li[0]

for i in range(1, len(li)):
    pli[i] = li[i] + pli[i-1]
#print(pli)

tmp = 0
#_len = float('inf')
ans = float('inf')
for i, e in enumerate(li):
    tmp += e
    if tmp>=s:
        ans = i + 1
        
        break


l = 0
r = 1

while l < r < n:
    if pli[r] - pli[l] < s:
        r+=1
    else:
        ans = min(ans, r - l)
        l+=1
        
    #print(f"l: {l}\tr: {r}\tlen: {ans}")

print(ans if ans != float('inf') else 0)