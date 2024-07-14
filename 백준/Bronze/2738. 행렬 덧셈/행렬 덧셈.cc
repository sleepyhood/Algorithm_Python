#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <map>
#include <vector>
#define MAX 101

using namespace std;

int arr[MAX][MAX];
int brr[MAX][MAX];

int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> brr[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << arr[i][j] + brr[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}
