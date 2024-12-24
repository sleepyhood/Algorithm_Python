# print("       _.-;;-._")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-;;-._|")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-''-._|")
"""
[백준]
2138. 전구와 스위치
https://www.acmicpc.net/problem/2138
"""

"""
0000

0101    (o) -> 1011-> 0111->0000
0100    (x) -> 1010-> 0100
"""
#0101

def switch(li, cnt):
    for i in range(1, n-1):
        if li[i-1]!=target[i-1]:
            cnt +=1
            li[i-1] = not li[i-1]
            li[i] = not li[i]
            li[i+1] = not li[i+1]

    if li[n-1]!=target[n-1]:
        cnt+=1
        li[n-2] = not li[n-2]
        li[n-1] = not li[n-1]

    if li == target:
        return cnt
    return -1

# 0번째 스위치를 눌렀는지, 안 눌렀는지에 따라 결과가 같이 변동
n = int(input())
off = list(map(bool, [int(i) for i in input()]))
target = list(map(bool, [int(i) for i in input()]))

on = off[:]
# 0번 스위치를 누른 경우
on[0] = not on[0]
on[1] = not on[1]


if off == target:
    print(0)
else:
    # 0번 스위치를 안 누를 경우
    count = switch(off, 0)
    if count != -1:
        print(count)
    else:
        # 0번 스위치를 누를 경우
        count = switch(on, 1)
        if count != -1:
            print(count)
        else:
            print(-1)
