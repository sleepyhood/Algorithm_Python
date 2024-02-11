_list = []
for _ in range(5):
    score = int(input())
    if score<40:
        _list.append(40)
    else:
        _list.append(score)
print(sum(_list)//5)