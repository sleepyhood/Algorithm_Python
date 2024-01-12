import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
arr = []

for _ in range(N):
    command = str(input().rstrip())
    x = 0
    if "push" in command:
        command, x = command.split()
        arr.append(int(x))
        
    elif command == "pop":
        if len(arr)==0:
            print("-1\n")
        else:
            print(f"{arr[0]}\n")           
            del arr[0]
    
    elif command == "size":
        print(f"{len(arr)}\n")
        
    elif command == "empty":
        if len(arr)==0:
            print("1\n")
        else:
            print("0\n")
            
    elif command == "front":
        if len(arr)==0:
            print("-1\n")
        else:
            print(f"{arr[0]}\n")    
            
    else: # back
        if len(arr)==0:
            print("-1\n")
        else:
            print(f"{arr[-1]}\n")              

    