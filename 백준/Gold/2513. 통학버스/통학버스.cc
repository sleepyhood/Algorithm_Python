#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath> // ceil() 사용을 위한 헤더 추가

using namespace std;

int n, k, s; // 아파트 개수(n), 통학 버스 정원(k), 학교 위치(s)
vector<pair<int, int>> apt; // (아파트 위치, 해당 아파트의 학생 수)
long long res = 0; // 총 이동 거리 결과

int main() {

    // 입력: 아파트 개수(n), 통학 버스 정원(k), 학교 위치(s)
    cin >> n >> k >> s;
    apt.resize(n);

    for (int i = 0; i < n; i++) {
        // 각 아파트의 위치와 해당 아파트에서 태워야 할 학생 수 입력
        cin >> apt[i].first >> apt[i].second;
    }

    // 아파트를 위치 기준으로 정렬 (왼쪽부터 오른쪽까지 순서대로 정렬)
    sort(apt.begin(), apt.end());

    int board = 0; // 현재 버스에 남아 있는 공간
    int i = 0;

    // 왼쪽 방향(학교보다 작은 좌표) 처리
    for (i = 0; i < n ; i++) {
        if (apt[i].first >= s) break; // 학교보다 오른쪽이면 루프 종료
        if (board >= apt[i].second) {
            // 남아 있는 공간이 현재 아파트의 학생 수보다 크거나 같으면 그대로 태우기
            board -= apt[i].second;
            continue;
        }
        
        // 부족한 학생 수만큼 버스에 태우고     이동 거리 계산
        apt[i].second -= board;
        res += ceil((double)apt[i].second / k) * (long long)(s - apt[i].first) * 2;
        //ceil(10.0 / 4)  // → 3. 3번왕복. * 학교위치-해당 태우는 위치(왕복거리) >>이동거리
        
        // 만약 k의 배수가 아니라면 남는 공간 저장(더 태울수 있는지)
        if (apt[i].second % k != 0) board = k - apt[i].second % k;
        else board = 0;
        
    }

    board = 0; // 오른쪽 아파트를 처리하기 위해 초기화

    // 오른쪽 방향(학교보다 큰 좌표) 처리
    for (int j = n - 1; j >= i; j--) {
        if (board >= apt[j].second) {
            // 남아 있는 공간이 현재 아파트의 학생 수보다 크거나 같으면 그대로 태우기
            board -= apt[j].second;
            continue;
        }

        // 부족한 학생 수만큼 버스에 태우고 이동 거리 계산
        apt[j].second -= board;
        res += ceil((double)apt[j].second / k) * (long long)(apt[j].first - s) * 2;

        // 만약 k의 배수가 아니라면 남는 공간 저장
        if (apt[j].second % k != 0) board = k - apt[j].second % k;
        else board = 0;
    }

    cout << res << "\n"; // 총 이동 거리 출력
}