"""
[백준]
16506. CPU
https://www.acmicpc.net/problem/16506
"""

import heapq
import sys
from collections import deque
# 무한대를 의미하는 값으로 충분히 큰 수를 설정합니다.
#INF = float('INF')

#input = sys.stdin.readline
#print = sys.stdout.write

# 10진법->2진법 문자열 리턴
def dec2Bin(n, byte=3):
    res = [0 for _ in range(byte)]
    n = int(n)

    while n>0:
        byte-=1
        res[byte] = n%2
        n//=2
    res = list(map(str, res))
    return ''.join(res)


n = int(input())
#m = int(input())
#li = list(map(int, input().split()))
li = []
res = []
for i in range(n):
    li.append(input().split())

# opcode
_dict = {'ADD': '0000', 'SUB':'0001', 'MOV':'0010', 'AND':'0011','OR':'0100', 'NOT':'0101', 'MULT':'0110','LSFTL':'0111', 'LSFTR':'1000','ASFTR':'1001','RL':'1010','RR':'1011'}

# ts = ['0111001000101000',
# '0110100111111100',
# '0101000100001000',
# '0001001001000110',
# '1001001101000010',
# '0110001111111010',
# '1010101101001110',
# '1011000011011000']

#idx = 0

for e in li:
    isConst = False
    tmp = ""

    if e[0][-1] == 'C':     
        # 4번 비트가 C인 경우, 15번 비트는 4자리 레지스터값이 들어감
        # 아닐 경우, 15번 비트는 0
        isConst = True

    if isConst: # 0~4번 bit
        tmp = _dict[e[0][:-1]] + '1'    # C를 제외한 명령어는 모두 동일하므로 슬라이싱
    else:
        tmp = _dict[e[0][:]] + '0'

    tmp+='0'    # 5번 bit

    tmp += dec2Bin(e[1])    # 6~8번 bit
    tmp += dec2Bin(e[2])    # 9~11번 bit

    if isConst: 
        tmp += dec2Bin(e[3], 4) # 12~15번 bit
    else:
        tmp += dec2Bin(e[3])    # 12~15번 bit
        tmp+='0'

    print(tmp)