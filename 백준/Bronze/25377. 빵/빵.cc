#include <iostream>
#include <algorithm>
using namespace std;
#define MAXLEN 1001

int a[MAXLEN];
int b[MAXLEN];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    int ans = 0;

    for (int i = 1; i <= n; i++) {
        cin >> a[i] >> b[i];
    }

    int idx = MAXLEN;
    for (int i = 1; i <= n; i++) { // 빵이 들어오는 시간은 a이다, b보다 커야함
        if (a[i] <= b[i]) {
            idx = min(idx, b[i]);
        }
    }

    if (idx == MAXLEN && a[1] > b[1]) {
        cout << -1 << "\n";
    }
    else {
        cout << idx << "\n";
    }


    return 0;
}