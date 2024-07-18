#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <map>
#include <vector>
#include <string>

#define MAX 500002

using namespace std;
long long l;    // 전체 가로등 개수
int n, k;       // 개수, 오름차순 개수

long long arr[MAX];
//int res[MAX];
map<long long, long long> m;  // 어두운 정도 각각 개수

int main() {
    cin >> l >> n >> k;
    int step = k;
    // 가로등이 있는 위치는 밝기가 0으로 고정
    // 가로등이 생길 때마다 1이 2번, 2가 2번씩 존재
    // 주의: 물어보는 양이 설치된 가로등보다 많을 수도 있음

    for (int i = 1; i <= n; i++) {
        long long tmp;
        cin >> tmp;
        arr[i] = tmp;
        m[0]++;
        step--;
    }
    arr[0] = 0;
    arr[n + 1] = l;
    /*
    10 2 10
    2 7
    */

    /*
        3번 조건
        N=3, L=12라 가정시 L/(N-1)=6
        A_1 = 0
        A_2 = 6
        A_3 = 12
    */

    /*
    3번 조건
    N=5, L=16라 가정시 L/(N-1)=4
    A_1 = 0
    A_2 = 4
    A_3 = 8
    A_4 = 12
    A_5 = 16
*/

    /*
    1000000000000000000 1 10
    100000000000000000
    */
    for (int i = 1; i <= n + 1; i++) {
        long long dif = arr[i] - arr[i - 1];
        if (dif < 0)
            dif *= -1;
        //cout << "dif: " << dif << endl;
        if (i == 1 || i == n + 1) {// 끝지점인 경우, 계속 어두워짐
            for (long long j = 1; j <= dif && step>=0; j++) {
                //cout << "j: "<<j << endl;
                m[j] += 1;
                step--;
                
            }
        }
        else {
            // 1 ~5 인경우, 1이 2번, 2가 1번 나옴
            if (dif % 2 == 0) {
                for (long long j = 1; j < dif / 2 && step >= 0; j++) {
                    //cout << "j: "<<j << endl;
                    m[j] += 2;
                    step--;
                }
                m[dif / 2] += 1;
                step--;
            }
            else {
                for (long long j = 1; j <= dif / 2 && step >= 0; j++) {
                    //cout << "j: "<<j << endl;
                    m[j] += 2;
                    step--;
                }
            }

        }
        /*if (step < 0)
            break;*/
    }

    for (auto e : m) {
        int len = e.second;
        for (int i = 0; i < len; i++) {
            cout << e.first;
            k--;
            if (k > 0)
                cout << "\n";              
            else
                return 0;
        }
        //if (k <= 0)
        //    break;
    }

    return 0;
}
