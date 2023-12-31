# 단어를 조합하되, 연속하여 발음은 불가
def solution(babbling):
    answer = 0
    sample = ["aya", "ye", "woo", "ma"]
    
#     고려할 것: ayamaaya인 경우에는 3이 나와야함.(연속만 안되면 됨)
    for word in babbling:
        temp = ''
        seq = 0
        isBabbling = True
        print(f"word: {word}")
        for s in sample:
            seq+=1
            word = word.replace(s, str(seq)).strip()

        for idx in range(len(word)):
            if ord(word[idx])>=ord('a') and ord(word[idx])<=ord('z'):
                isBabbling = False
                break
                
        if isBabbling:
            for idx in range(len(word)-1):
                if word[idx]==word[idx+1]:
                    isBabbling = False
                    break
                
        if isBabbling:
            answer+=1
        # print(temp)
    
    # st = 'abcde'
    # print(st.replace('abc', str(1)).strip())

    return answer