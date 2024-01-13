import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
cardArr = input().rstrip()
cardArr = list(map(int, cardArr.split()))

cardDict = {}

for i in range(len(cardArr)):
    if cardArr[i] not in cardDict.keys(): # 갯수가 중요하므로, 기존에 있는 카드면 누적
        cardDict[cardArr[i]] = 1
  

m = int(input().rstrip())
findArr = input().rstrip()
findArr = list(map(int, findArr.split()))

for card in findArr:
    if card in cardDict.keys():
        print(f"{cardDict[card]} ")
    else:
        print(f"0 ")

print("\n")        
