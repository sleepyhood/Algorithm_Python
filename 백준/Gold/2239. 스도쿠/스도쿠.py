import sys

sys.setrecursionlimit(10000)


def check(value, r, c):
    global li
    # 열 체크
    for i in range(9):
        if li[r][i] == value:
            #print(f"row : {li[r][i]}")
            return False

    # 행 체크
    for i in range(9):
        if li[i][c] == value:
            #print(f"row : {li[i][c]}")
            return False

    # 3*3 체크

    sr = r//3 * 3
    sc = c//3 * 3
    er = sr + 3
    ec = sc + 3

    for i in range(sr, er):
        for j in range(sc, ec):
            if li[i][j] == value:
                return False

    return True

def fun(idx):
    global li
    global zeros

    if idx == len(zeros):
        for i in range(9):
            for j in range(9):
                print(li[i][j], end='')
            print()
        exit()

    # 해당 위치에서, 1~9 사이의 값을 넣어봐야 한다.
    # 아니라면, 해당 위치는 초기화

    r = zeros[idx][0]
    c = zeros[idx][1]
    for k in range(1, 10):
        # 이 자리에 넣어도 괜찮은지
        if check(k, r, c):
            li[r][c] = k
            fun(idx+1)
            li[r][c] = 0
           
    return

li = [0]*9

for i in range(9):
    tmp = input()
    li[i] = [int(e) for e in tmp]


zeros = []  # 0인 좌표들
for i in range(9):
    for j in range(9):
        if li[i][j] == 0:
            zeros.append([i,j])

fun(0)