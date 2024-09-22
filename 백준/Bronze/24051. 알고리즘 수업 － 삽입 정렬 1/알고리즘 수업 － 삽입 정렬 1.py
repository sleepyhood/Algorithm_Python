from collections import deque
import sys
#import bisect
"""
[백준]
24051. 알고리즘 수업 - 삽입 정렬 1
https://www.acmicpc.net/problem/24051
"""

input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().split())
li = list(map(int, input().split()))

"""
insertion_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for i <- 2 to N {
        loc = i - 1;
        newItem = A[i];

        # 이 지점에서 A[1..i-1]은 이미 정렬되어 있는 상태
        while (1 <= loc and newItem < A[loc]) {
            A[loc + 1] <- A[loc];
            loc--;
        }
        if (loc + 1 != i) then A[loc + 1] = newItem;
    }
}
"""
cnt = 1
ans = 0
for i in range(1, len(li)):
    newItem = li[i] 
    loc = i - 1
    #print(f"{li}\n")

    while loc>=0 and li[loc]>newItem:   # 왼쪽 원소가 더 클 때만 이동
        li[loc+1] = li[loc]     # 현재 원소를 오른쪽으로 옮김
        if cnt == k:
            ans = li[loc+1]
        #print(f"{cnt}. li[loc+1]{li[loc+1]}\n")
        loc-=1
        cnt+=1
        #print(f"{li}\n")
    
    if  loc + 1 != i :
        li[loc+1] = newItem
        if cnt == k:
            ans = li[loc+1]
    #print(f"{cnt}. li[loc+1]{li[loc+1]}\n")
        cnt+=1

#print(f"{li}\n")

if ans!=0:
    print(f"{ans}\n")
else:
    print(f"{-1}\n")