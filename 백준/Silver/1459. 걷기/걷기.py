x, y, w, s =map(int, input().split())
# 한 블록 가는데 걸리는 시간 W와 대각선으로 한 블록을 가로지르는 시간 S
'''
가로 4
세로 2

=> 대각선 2+가로 2 vs 가로4 + 세로2
 = 10*2+2*3 vs 3*4+3*2 = 12 + 6 = 18

=> 대각선 2+가로 2 vs 가로4 + 세로2


예외처리: 
가로세로가 아닌, 대각선으로만 이동하는게 더 유리할 경우:
-> 심지어, 기울기가 같지 않고, \/ 와 같이 다시 노선 변경이 가능하다.
'''

m = (min(x,y))   # 대각선으로 가는 길이
# other = max(x, y) - m

# route1 = other *w + m*s
# route2 = x*w + y*w

result = x*w + y*w
remain = max(x, y) - min(x, y)  # 남은 거리

# 방법 1: 일단 최소 대각선 이동 해보고, 나머지는 그냥 걷기
#print(f"그냥 블록: {result}")
# 대각선을 타는게 더 빠른지 체크 (1번 쓰기~m번 쓰기)
#for i in range(1, min(x,y)+1):
result = min (result , m*s + remain*w)
#    print(f"대각선 {i} 개 이동: {((x-i)+(y-i)) * (w) + s * i}")


# 방법 2: 대각선 도달 후, 남은 거리도 대각선으로만 이동하기
tmp = (min(x, y)) * (s)

ttmp = remain%2
result = min(result, tmp + remain//2 * s * 2 + ttmp*w)
    
print(result)

# 122 * 29 + 7