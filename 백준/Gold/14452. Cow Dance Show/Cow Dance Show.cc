#include <stdio.h>
#include <algorithm>
#include <queue>

int arr[10000] = {};
int n = 0, t = 0;

int f(int m) {
    std::priority_queue<int, std::vector<int>, std::greater<int>> q;
    int maxTime = 0;

    for (int i = 0; i < n; i++) {
        q.push(maxTime + arr[i]);  // 현재 공연 종료 예상 시간 추가
        if (q.size() >= m) {  // 무대에 올릴 수 있는 최대 인원 초과 시
            maxTime = std::max(maxTime, q.top());
            q.pop();
        }
    }

    while (!q.empty()) {  // 남은 학생들의 최대 종료 시간 갱신
        maxTime = std::max(maxTime, q.top());
        q.pop();
    }

    if (maxTime > t)
        return 0;  // T시간을 초과하면 불가능
    else if (maxTime == t)
        return 1;  // 정확히 T시간이면 가능
    else
        return 2;  // T시간 이하로 가능
}

int main() {
    scanf("%d %d", &n, &t);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int s = 1, e = n;
    int ans = n;  // 최솟값을 찾으므로 최대 학생 수부터 시작

    while (s <= e) {
        int m = (s + e) / 2;
        int ck = f(m);

        if (ck) {  // 가능하면 정답 후보 저장하고 더 작은 k를 탐색
            ans = m;
            e = m - 1;
        } else {  // 불가능하면 k를 더 증가
            s = m + 1;
        }
    }

    printf("%d", ans);
    return 0;
}