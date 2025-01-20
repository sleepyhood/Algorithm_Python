# print("       _.-;;-._")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-;;-._|")
# print("'-..-'|   ||   |")
# print("'-..-'|_.-''-._|")
"""
[백준]
11758. CCW
https://www.acmicpc.net/problem/11758
"""
x1, y1 = map(int, (input().split()))
x2, y2 = map(int, (input().split()))
x3, y3 = map(int, (input().split()))

result = (x2 - x1) * (y3 - y1) - (y2-y1) * (x3-x1)

print(1 if result > 0 else -1 if result < 0 else 0)