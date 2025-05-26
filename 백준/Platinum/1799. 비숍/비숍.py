

def back(idx, cnt, color):
    global result

    if idx == len(cells[color]):
        colors[color] = max(colors[color], cnt)
        return

    # for i in range(len(bishops)):

    r = cells[color][idx][0]
    c = cells[color][idx][1]

    left  = r - c + (n-1)          # r+c = 2 -> (0,2), (1,1), (2,0)
    right = r + c     # r-c = 0 -> (0,0), (1,1), (2,2)


    if left not in left_dia and right not in right_dia:
        left_dia.add(left)
        right_dia.add(right)
        
        #visit[i] = True

        back(idx + 1, cnt+1, color)

        #visit[i] = False
        left_dia.remove(left)
        right_dia.remove(right)
    back(idx + 1, cnt, color)
    #check()


n = int(input())

li = [0] * n
bishops = []    # 비숍의 위치 저장
#visited = [[False] * n for i in range(n)]

for i in range(n):
    li[i] = list(map(int,input().split()))

# 좌표를 흑/백으로 나누기
cells = [[], []]  # 0: black, 1: white
for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            color = (i + j) % 2
            cells[color].append((i, j))



# 중요: 비숍은 서로 같은 색상의 칸에서만 충돌 가능
#print(bishops)
left_dia = set()        # 행-열의 값으로 왼쪽 대각선 기울기 저장
right_dia = set()        # 행+열의 값으로 오른쪽 대각선 기울기 저장

colors = [0, 0]

# 블랙 칸
back(0, 0, 0)

# 흰색 칸
back(0, 0, 1)
print(sum(colors))
