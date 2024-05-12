#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

#define MAXLEN 100001

long arr[MAXLEN];
long sumArr[MAXLEN];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    long n, m;
    cin >> n >> m;

    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
        sumArr[i] = arr[i] + sumArr[i - 1];
    }

    while (m--) {
        long i, j;
        cin >> i >> j;
        cout << sumArr[j] - sumArr[i-1] << "\n";
    }

    return 0;
}