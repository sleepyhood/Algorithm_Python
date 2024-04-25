#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int n = 0;
	cin >> n;


	int* arr = new int[n];
	int sum = 0;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		sum += arr[i];
	}


	// 정렬
	sort(arr, arr + n);

	int x = 0;
	int ans = 0;
	cin >> x;
	// 찾아야 하는값 x
	
	int l = 0;
	int r = n - 1;

	while (l < r) {
		if (arr[l] + arr[r] < x) {
			l++;
		}
		else if(arr[l] + arr[r] > x) {
			r--;
		}
		// 같은 경우
		else{
			l++;
			r--;
			ans++;
		}
	}
	cout << ans << endl;
	// 시간 복잡도 O(n^2) 은 사용 불가

	/*for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			if (arr[i] + arr[j] == x) {
				ans++;
			}
		}
	}*/

//cout << ans << endl;
	return 0;
}