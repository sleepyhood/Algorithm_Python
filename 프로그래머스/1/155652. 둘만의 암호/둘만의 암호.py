# ord: char to int  (아스키 코드)
# chr: int to char  (아스키 코드)
def solution(s, skip, index):
    answer = ''
    for i in s:
        intAscii = ord(i)
        for j in range(index):
            intAscii+=1

            if intAscii > ord('z'):
                intAscii = intAscii - ord('z') + ord('a') - 1
                
            while chr(intAscii) in skip:
                if intAscii > ord('z'):
                    # print(i)
                    intAscii = intAscii - ord('z') + ord('a') - 1
                intAscii+=1
                
            if intAscii > ord('z'):
                intAscii = intAscii - ord('z') + ord('a') - 1
                
            while chr(intAscii) in skip:
                if intAscii > ord('z'):
                    # print(i)
                    intAscii = intAscii - ord('z') + ord('a') - 1
                intAscii+=1

        answer+=(chr(intAscii))
    return answer