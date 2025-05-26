#include <iostream>
#include <climits>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

typedef long long ll;
pair<int, int> arr[100'001];
unordered_map<int, int> cntX, cntY;

/*

cntX[x]: x좌표가 x인 점들의 개수

cntY[y]: y좌표가 y인 점들의 개수

*/
/*

예를 들어 (3,4)를 기준으로,

x=3인 점: (3,5)

y=4인 점: (5,4), (4,4)

(3,4)를 기준으로 만들 수 있는 나이스 삼각형 수: 1 * 2 = 2

이렇게 모든 점에 대해 반복해서 더하면, 최종 답은 4

*/

int main() {
	int n;

	cin >> n;

	for (int i = 0; i < n; i++) {
		int x, y;
		cin >> x >> y;
		arr[i] = { x, y };
		cntX[x]++;
		cntY[y]++;
	}

	ll total = 0;

	for (int i = 0; i < n; i++) {
		int x = arr[i].first;
		int y = arr[i].second;

		ll cx = cntX[x] - 1;
		ll cy = cntY[y] - 1;

		total += cx * cy;
	}

	cout << total;

}
