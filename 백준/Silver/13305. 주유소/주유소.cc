#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

/* 
* 
* 반례: 현재 지점에서 주유를 안 하는 경우도 존재
* 
4
1000 1000 1000
2 5 1 4	

2*2000 + 1*1000

5000

*/

long road[100000];
long price[100001];

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n - 1; i++)
	{
		cin >> road[i];
	}

	for (int i = 0; i < n; i++)
	{
		cin >> price[i];
	}

	long total_cost = 0;
	long min_price = price[0];

	for (int i = 0; i < n - 1; i++) {
		// 현재까지의 최소 가격으로 필요한 기름만 주유
		total_cost += min_price * road[i];

		// 현재 도시의 주유소 가격이 더 싸면 최소값 갱신
		if (price[i + 1] < min_price) {
			min_price = price[i + 1];
		}
	}
	cout << total_cost << endl;
	
	return 0;
}