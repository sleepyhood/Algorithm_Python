#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <map>
#include <vector>
#define MAX 10000001

using namespace std;

int arr[MAX];

//void init() {
//    for (int i = 2; i <= 30; i++) {
//        for (int j = 2; j < i; j++) {
//            if (i % j == 0)
//                arr[i]++;
//        }
//    }
//}
vector <long long> v;

long long gcd(long long a, long long b) {
    long long c = a % b;
    
    while (c != 0) {
        a = b;
        b = c;

        c = a % b;
    }

    return b;
}

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        long long tmp;
        cin >> tmp;
        v.push_back(tmp);
    }
    sort(v.begin(), v.end());

    if (v.size() == 1) {
        cout << v[0] * v[0] << endl;
    }
    else {
        cout << v[0] * v[n - 1] << endl;
    }

    //for (int i = 0; i < n - 1; i++) {
    //    long long res = gcd(v[i], v[i + 1]);
    //    long long lcm = v[i] * v[i + 1] / res;

    //    if (lcm == v[i+1]) {
    //        
    //        v[i + 1] = v[i] * v[i + 1];
    //    }
    //    else {
    //        v[i + 1] = v[i] * v[i + 1] / res;
    //    }
    //    cout << v[i + 1] << endl;
    //}
    //cout << v[n - 1] << endl;

    return 0;
}
