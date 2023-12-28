def solution(n, times):
    answer = 0
    start = 1
    end = max(times) * n

    times.sort()

    while start <= end:
        cnt = 0
        mid = (start + end) // 2

        for t in times:
            cnt += mid // t

        if cnt >= n:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1

    return answer
