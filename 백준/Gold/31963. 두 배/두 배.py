import math
n= int(input())
li = list(map(int, input().split()))
ans =0 
 #difference list
diff = [0]*(n-1)
 
for i in range(n-1):
    diff[i]=li[i+1] - li[i]
         # not increase
    if diff[i] <0: 
        k = math.ceil(math.log2(li[i]/li[i+1]))
        ans+=k
        #print(k)
        #ans+=abs(diff[i]//2)+1
        #li[i+1] = li[i+1] *(2**(abs(diff[i]//2)+1))
        li[i+1]*=(2**k)
        diff[i] = li[i+1]-li[i]
print(ans)