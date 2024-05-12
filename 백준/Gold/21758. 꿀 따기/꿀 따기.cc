#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;
//꿀따기

#define MAXLEN 100001

long arr[MAXLEN];
long sumArr[MAXLEN];

int main()
{
    long n;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
        sumArr[i] = arr[i] + sumArr[i - 1];
    }

    long ans = 0;
    // 벌은 최대한 꿀통과 멀리 있어야 유리
    // i) 벌꿀벌인 경우
    // ii) 벌벌꿀인 경우
    // iii) 꿀벌벌인 경우
    for (int i = 2; i < n; i++) {
        ans = max(ans, sumArr[i] - arr[1] + sumArr[n - 1] - sumArr[i - 1]);
        ans = max(ans, sumArr[n] - arr[1] - arr[i] + sumArr[n] -  sumArr[i]);
        ans = max(ans, sumArr[n - 1] - arr[i] + sumArr[i - 1]);
    
    }
    cout << ans << "\n";

    return 0;
}