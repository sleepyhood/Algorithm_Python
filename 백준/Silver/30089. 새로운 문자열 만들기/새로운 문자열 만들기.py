line = input().strip()
n = int(line)

for _ in range(n):
    s = input().strip()
    length = len(s)
    rev_s = s[::-1]  # S를 뒤집은 문자열 미리 생성
        
    max_overlap = 0 # 겹치는 길이 저장 변수

    # [바깥 for문] 겹치는 길이(i)를 전체 길이부터 0까지 줄여가며 시도
    for i in range(length, -1, -1):
        is_match = True
            
        # [안쪽 for문] 길이 i만큼 실제로 글자가 같은지 검사
        # S의 뒷부분 vs rev_s의 앞부분 비교
        for j in range(i):
            # S는 뒤에서부터 i개 구간을 봐야 하므로 인덱스는 (length - i + j)
            # rev_s는 앞에서부터 봐야 하므로 인덱스는 j
            # print(s, s[length - i + j]+'\n'+rev_s, rev_s[j], '\n')
            if s[length - i + j] != rev_s[j]:
                is_match = False
                break # 하나라도 다르면 즉시 중단 (다음 overlap 길이로 이동)
        # print("===========")    
        # 안쪽 for문을 무사히 통과했다면(is_match가 True라면)
        # 현재 i가 가능한 가장 긴 겹침 길이임 (바깥 루프가 큰 수부터 시작했으므로)
        if is_match:
            max_overlap = i
            break # 정답을 찾았으므로 바깥 루프 종료

    # 정답 출력: 원래 문자열 + (겹치지 않는 나머지 뒷부분)
    # rev_s에서 앞의 max_overlap만큼은 이미 s에 포함되었으므로 그 뒤만 붙임
    result_suffix = ""
    for k in range(max_overlap, length):
        result_suffix += rev_s[k]
            
    print(s + result_suffix)
