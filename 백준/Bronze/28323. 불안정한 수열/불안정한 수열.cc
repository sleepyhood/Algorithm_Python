#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#define MAX 300001

using namespace std;

int arr[MAX];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;
    
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }

    int result = n;
    //int st = arr[1];
    // ① 짝 홀 짝 홀 인 경우

    for (int i = 2; i <= n; i++) {
        if ((arr[i - 1] % 2 == 0 && arr[i] % 2 == 0) || (arr[i - 1] % 2 != 0 && arr[i] % 2 != 0)) {
            result--;
        }
    }

    //int result = max(max1, max2);
    //cout << max1 << "\t"<<max2 << endl;
    cout << result << endl;
    return 0;
}
