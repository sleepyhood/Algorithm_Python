#include <iostream>
#include <algorithm>
using namespace std;
#define MAXDISHES 3000001
#define MAXKINDS 3001

int dishes[MAXDISHES];
int kinds[MAXKINDS];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    /*
    첫 번째 줄에는 회전 초밥 벨트에 놓인 접시의 수 N, 
    초밥의 가짓수 d, 
    연속해서 먹는 접시의 수 k, 
    쿠폰 번호 c가 각각 하나의 빈 칸을 사이에 두고 주어진다. 
    */

    int n, d, k, c;
    cin >> n >> d >> k >> c;

    for (int i = 1; i <= n; i++) {
        int dish;
        cin >> dish;
        dishes[i] = dish;   // 실제 접시 배열
    }
    
    // 슬라이딩 윈도우 방식과 매우 유사
    int ans = 0;

    // 첫 구간 슬라이딩
    for (int i = 1; i <= k; i++) {
        kinds[dishes[i]]++;         // 한 번 돌 때마다 먹었다라고 처리함
        if (kinds[dishes[i]] == 1) { // 각 접시별 중복 여부(먹어본 그릇은 세지않음)
            //kinds[dishes[i]]--;
            ans++;
        }
            
    }

    
    kinds[c]++;
    if (kinds[c] == 1) ans++;
    int maxVal = ans;

    // 양옆만 움직이므로, 구간내 그릇을 모두 0으로 초기화하면 안됌
    for (int i = 1; i < n ; i++) {
        int l = i;
        int r = (i + k) <= n ? (i + k) : (i + k - n);

        kinds[dishes[l]]--;
        if (kinds[dishes[l]] == 0) {
            ans--;
        }
        kinds[dishes[r]]++; // 새로 본 접시 중복 여부(먹어본 그릇은 세지않음)
        
        if (kinds[dishes[r]] == 1) { 
            ans++;
        }
        

            
        maxVal = max(maxVal, ans);
        
        
    }

    cout << maxVal <<"\n";
    
    return 0;
}
