#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <set>
#define MAX 1000000000000000001
#define LAMPMAX 300001

using namespace std;
long long l;    // 전체 가로등 개수
int n, k;       // 개수, 오름차순 개수

long long arr[LAMPMAX];
//int res[MAX];
map<long long, int> visit;      // 위치별 방문 여부
map<long long, long long> m;    // 어두운 정도 각각 개수

queue<pair<long long, long long>> q;

/*
100000000000 2 5000
99999999997
99999999999
*/
int main() {
    cin >> l >> n >> k;
    long long lampCnt = 0;
    // 가로등이 있는 위치는 밝기가 0으로 고정
    // 가로등이 생길 때마다 1이 2번, 2가 2번씩 존재
    // 주의: 물어보는 양이 설치된 가로등보다 많을 수도 있음
    for (int i = 0; i < n; i++) {
        long long tmp;
        cin >> tmp;
        arr[i] = tmp;           // 위치를 기억해야 중복을 방지할 수 있다.
        q.push({ tmp, 0 });
        //m[tmp]++;               // 위치당 가로등 수
    }

    while (lampCnt<k && q.size()) {
        long long lampLoc = q.front().first;
        long long darkness = q.front().second;
        q.pop();
        
        if (visit.count(lampLoc) == 1) {
            //cout << "!" << endl;
            continue;
        }
        //if (m[lampLoc] > 1) {       // 해당 위치에 방문을 했다면
        //    continue;
        //}
        visit[lampLoc] = 1;             // 중복된 위치는 못 가게
        m[darkness]++;
        //cout << darkness << "\n";

        if (lampLoc - 1 >= 0) {
            q.push({ lampLoc - 1, darkness + 1 });
        }
        if (lampLoc + 1 <= l) {
            q.push({ lampLoc + 1, darkness + 1 });
        }
        lampCnt++;
    }

    lampCnt = 0;
    for (auto e : m) {
        int len = e.second;
        for (int i = 0; i < len; i++) {

            if (lampCnt >= k) {
                return 0;
            }
            cout << e.first << "\n";
            lampCnt++;
        }
        //if (k <= 0)
        //    break;
    }

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

/*
100000000000 2 5000
99999999997
99999999999
*/

/*
100000000000 3 5000
99999999900
99999999997
99999999999
*/

/*
1000000000000000000 3 50
333333333333333333
555555555555555555
999999999999999999


*/
    return 0;
}
