#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#define MAX 500001
using namespace std;

int red[MAX];
int blue[MAX];

int main()
{
	int n = 0;
	cin >> n;
	//cin.ignore();
	
	string input;
	cin >> input;
	
	// 빨강은 1, 파랑은 0
	for (int i = 1; i <= n; i++) {
		red[i] += red[i - 1];
		blue[i] += blue[i - 1];

		if (input[i-1] == 'R')
			red[i]++;
		else
			blue[i]++;
	}

	/*
		2가지 경우가 존재
		1. 빨강이 왼쪽, 파랑이 오른쪽
		2. 빨강이 오른쪽, 파랑이 왼쪽
	*/

	// 1. 빨강이 오른쪽인 경우
	int res = MAX;
	for (int i = 1; i <= n; i++) {
		res = min(res, red[i] + blue[n] - blue[i]);
	}
	// 2. 빨강이 왼쪽인 경우
	for (int i = 1; i <= n; i++) {
		res = min(res, blue[i] + red[n] - red[i]);
	}
	cout << res << endl;
	/*for (int i = 1; i <= n; i++) {
		cout << red[i] << " ";
	}
	cout << "\n";
	for (int i = 1; i <= n; i++) {
		cout << blue[i] << " ";
	}*/
	return 0;
}