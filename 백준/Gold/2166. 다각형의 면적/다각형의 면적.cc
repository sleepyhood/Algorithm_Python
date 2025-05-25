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

Point arr[100'01];


int main()
{
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; i++) cin >> arr[i].x >> arr[i].y;

	// 신발끈 공식: (x0*y1+x1*y2+...) - (y0*x1+y1*x2+...)

	ll sum1 = 0, sum2 = 0;

	for (int i = 0; i < n; i++) {
		sum1 += arr[i].x * arr[(i+1) % n].y;
		sum2 += arr[i].y * arr[(i+1) % n].x;

	}

	double res = abs(sum1 - sum2) / 2.0;

	printf("%.1lf", res);
}