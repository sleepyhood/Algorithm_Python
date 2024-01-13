import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
cardArr = input().rstrip()
cardArr = list(map(int, cardArr.split()))

cardDict = {}

for i in range(len(cardArr)):
    if cardArr[i] in cardDict.keys():
        cardDict[cardArr[i]] += 1
    else:
        cardDict[cardArr[i]] = 1        

m = int(input().rstrip())
findArr = input().rstrip()
findArr = list(map(int, findArr.split()))

cardArr = list(set(cardArr))

for card in findArr:
    if card in cardDict.keys():
        print(f"{cardDict[card]} ")
    else:
        print(f"0 ")

print("\n")        
#for item in answer:
 #   print(f"{itemp} ")