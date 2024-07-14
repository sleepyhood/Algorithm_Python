#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <map>
#include <vector>
#define MAX 100

using namespace std;

vector<int> v;

int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        v.push_back(i);
    while (m--) {
        int l, r;
        cin >> l >> r;

        int tmp = v[l - 1];
        v[l - 1] = v[r - 1];
        v[r - 1] = tmp;
        //reverse(v.begin() + (l - 1), v.begin() + r);
    }


    //reverse(v.begin() + 1, v.end() - 1);
    for (auto e : v) {
        cout << e << " ";
    }

    return 0;
}
