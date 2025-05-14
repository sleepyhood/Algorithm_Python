#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
using namespace std;

typedef long long ll;
ll n;

struct Point {
	ll x;
	ll y;
};

Point arr[100'001];
vector<Point> u, d;  // 위쪽과 아래쪽


ll ccw(const Point& p1, const Point& p2, const Point& p3) {
	ll a = (p2.x - p1.x) * (p3.y - p1.y);
	ll b = (p3.x - p1.x) * (p2.y - p1.y);

	if (a - b > 0)       return 1;      // 반시계 방향
	else if (a - b < 0)  return -1;     // 시계 방향
	else                 return 0;      // 일직선(문제에서는 존재하지 않는다.)
}

ll cmp(const Point& p1, const Point& p2) {
	if (p1.x == p2.x) return p1.y < p2.y;
	return p1.x < p2.x;
}

ll Monotone_Chain() {

	// 아래껍질
	// 반시계방향
	// 가장 x 좌표가 작은 것부터 보기.
	// 일직선 위의 점은 버리지 않는다.
	for (int i = 0; i < n; i++) {
		while (d.size() >= 2) {
			Point p1 = d[d.size() - 1];
			Point p2 = d[d.size() - 2];
			if (ccw(p2, p1, arr[i]) <= 0) {		// 시계방향
				d.pop_back();
			}
			else {
				break;
			}
		}
		d.push_back(arr[i]);
	}

	// 위껍질
	// x좌표 큰 것부터 보기
	// 역순이므로 시계방향인 것을 제외하기
	// 일직선 위의 점은 버리지 않는다.
	for (int i = n - 1; i >= 0; i--) {
		while (u.size() >= 2) {
			Point p1 = u[u.size() - 1];
			Point p2 = u[u.size() - 2];
			if (ccw(p2, p1, arr[i]) <= 0) {
				u.pop_back();
			}
			else {
				break;
			}
		}
		u.push_back(arr[i]);
	}

	vector<Point> hull; // 전체 점 저장
	set<pair<int, int>> visited;    // 점 방문 여부

	for (Point e : d) {
		if (!visited.count({ e.x, e.y })) {
			visited.insert({ e.x, e.y });
			hull.push_back(e);
		}
	}

	for (Point e : u) {
		if (!visited.count({ e.x, e.y })) {
			visited.insert({ e.x, e.y });
			hull.push_back(e);
		}
	}
	/*for (Point e : hull) {
		cout << e.x << " " << e.y << "\n";
	}*/
	return hull.size();
}

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; i++) cin >> arr[i].x >> arr[i].y;

	sort(arr, arr + n, cmp);

	// 껍질 구하기
	ll result = Monotone_Chain();

	cout << result;
}