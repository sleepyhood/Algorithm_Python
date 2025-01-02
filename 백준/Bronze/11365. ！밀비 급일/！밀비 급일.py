while True:
    s = input()
    if s== "END":
        break
    s = list([i for i in s])
    s.reverse()
    print(''.join(s))