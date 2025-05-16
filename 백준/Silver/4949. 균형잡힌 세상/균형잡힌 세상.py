#val1, val2 = map(int,input().split())

#val1 = int(val1)
#val2 = int(val2)


while True:
    s = input()
    if len(s) == 1 and s == '.':
        break

    st = []
    balnce = 0

    for e in s:
        if e == '(':
            st.append('(')
            balnce+=1
        elif e == ')' :
            if len(st) and '(' == st[-1]:
                st.pop()
                balnce-=1
            else:
                balnce = -1
                break

        elif e == '[':
            st.append('[')
            balnce+=1
        elif e == ']' :
            if len(st) and '[' == st[-1]:
                st.pop()
                balnce-=1
            else:
                balnce = -1
                break
    if len(st) == 0 and balnce == 0: 
        print("yes")
    else:
        print("no")
