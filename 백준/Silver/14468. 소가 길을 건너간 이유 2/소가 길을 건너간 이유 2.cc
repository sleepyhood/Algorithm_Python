#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

using namespace std;

int main()
{
	char arr[52] = {};
	pair<int, int> a[52] = {};

	string s;
	cin >> s;

	for (int i = 0; i < 52; i++) {
		a[i].first = a[i].second = -1;
	}

	for (int i = 0; i < s.length(); i++) {
		int idx = s[i] - 'A';
		if (a[idx].first == -1) {
			a[idx].first = i;
		}

		else {
			a[idx].second = i;
		}

	}

	int ans = 0;

	for (int i = 'A'; i <= 'Z'; i++) {
		for (int j = 'A'; j <= 'Z'; j++) {

			int s1 = a[i - 'A'].first;
			int e1 = a[i - 'A'].second;
			int s2 = a[j - 'A'].first;
			int e2 = a[j - 'A'].second;

			if (i == j) {

			}

			else if (e2 < s1) {
				// 범위를 벗어난 경우1 (왼쪽)
			}
			else if (s2 > e1) {
				// 범위를 벗어난 경우2 (오른쪽)
			}
			else if ((s2 > s1 && e2 < e1) || (s2 < s1 && e2 > e1)) {
				// 종속된 경우
				// s1e1에 s2e2가 포함되거나 s2e2에 s1e1가 포함된 경우
			}

			//else if ((s2 < s1 && s2 < e1 && e2 > s1 && e2 < e1) || (s2 > s1 && s2< e1 && e2 > e1 && e2 > s1)) {
			else{
				//printf("a[i]: %c\ns1: %3d e1: %3d\na[j]: %c\ns2: %3d e2: %3d\n\n", i, s1, e1, j, s2, e2);
				ans++;
			}


		}
	}
	cout << ans / 2;


	return 0;
}