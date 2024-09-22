from collections import deque
import sys
"""
[백준]
12015. 가장 긴 증가하는 부분 수열2
https://www.acmicpc.net/problem/12015
"""

input = sys.stdin.readline
print = sys.stdout.write
import bisect

def length_of_lis(arr):
    lis = []  # 증가하는 부분 수열을 저장할 리스트
    
    for num in arr:
        # lis에서 num이 들어갈 위치를 찾음
        pos = bisect.bisect_left(lis, num)
        #print(f"num: {num}\tpos: {pos}\n")
        # lis의 끝에 num을 추가하거나, 기존 값을 num으로 바꿈
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
    
    return len(lis)

n = int(input())
arr = list(map(int, input().split()))
print(f"{length_of_lis(arr)}\n")  # 출력: 4
