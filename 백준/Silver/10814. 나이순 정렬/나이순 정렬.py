import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
my_list = []
#_dict = {}

for i in range(N):
    age, name = (input().rstrip()).split()
    age = int(age)
    my_list.append([i, age, name])
    #_dict[i] = []
    #_dict[i]+=[age, name]
    
sorted_list = sorted(my_list, key=lambda x: (x[1], x[0]))
    
for i in range(len(sorted_list)):
    print(f"{sorted_list[i][1]} {sorted_list[i][2]}\n")
    
#print(f"{sorted_list}\n")   
    