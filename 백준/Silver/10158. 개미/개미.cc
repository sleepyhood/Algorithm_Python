#include<iostream>
using namespace std;
int main()
{
	long long w = 0;
	long long h = 0;
	long long p = 0;
	long long q = 0;
	long long t = 0;
	cin >> w >> h;
	cin >> p >> q;
	cin >> t;


		p = (p + t) % (2 * w);
		if (p > w) {
			p = (2 * w) - p;
        }
	

		q = (q + t) % (2 * h);
		if (q > h) {
			q = (2 * h) - q;
        }
	//if (q < 0)
	//{
	//	q *= -1;
	//}
	//if (p < 0)
	//{
	//	p *= -1;
	//}
	cout << p << ' ' << q;
}