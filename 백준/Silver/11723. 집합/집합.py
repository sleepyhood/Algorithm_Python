import sys

print = sys.stdout.write
input = sys.stdin.readline

M = int(input().rstrip())
s = set([])#집합 



for _ in range(M):
    command = input().rstrip()
    if command == "empty" or command == "all":
        pass
    else:
        command, x = command.split()
        x = int(x)
        
    if command == "add":
        s.update({x})
    elif command == "check":
        if x in s:
            print('1\n')
        else:
            print('0\n')
    elif command == "remove" and x in s:    # remove 메소드는 에러발생
        s.discard(x)
        
    elif command == "toggle":
        if x in s:
            s.discard(x)
        else:
            s.add(x)
    elif command == "empty" and len(s)>0:
        s = set([])#집합 

    elif command == "all":
        if all(i in s for i in range(1, 21)):
            continue
        s = set([])#집합 
        for i in range(1, 21):
            s.add(i)
   
    
