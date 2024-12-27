
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <set>
using namespace std;

int arr[10000];
int n, k;
int cnt;

int main()
{
	cin >> n >> k;
	for (int i = 0; i < n; i++)
		cin >> arr[i];

	for (int i = n - 1; i >= 0; i--)
	{
		int maxVal = arr[i];
		int maxIdx = i;
		// arr[i]를 전제 구간의 최대라 가정
		for (int j = 0; j <= i; j++)
		{
			if (arr[j] > maxVal)
			{
				maxVal = arr[j];
				maxIdx = j;
			}
		}
		if (maxIdx != i)	// 교환하는 경우
		{
			int t = arr[maxIdx];
			arr[maxIdx] = arr[i];
			arr[i] = t;
			cnt++;
		}
		if (cnt == k)
		{
			for (int i = 0; i < n; i++)
				cout << arr[i] << " ";
			return 0;
		}
	}
	cout << -1;
	return 0;
}