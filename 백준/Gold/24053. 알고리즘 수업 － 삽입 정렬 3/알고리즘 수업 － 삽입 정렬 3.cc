
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <set>
using namespace std;

int arr[10000];
int after[10000];
int cnt = 1;

void printArr(int n)
{
	cout << cnt << ": ";
	for (int i = 0; i < n; i++)
	{
		cout << arr[i] << " ";
	}
	cout << "\n";
	cnt++;
}

bool compareArr(int n)
{
	for (int i = 0; i < n; i++)
	{
		if (arr[i]!= after[i])
			return false;
	}
	return true;
}

int main()
{
	int n;
	bool check = false;
	cin >> n;

	for (int i = 0; i < n; i++)
		cin >> arr[i];
	for (int i = 0; i < n; i++)
		cin >> after[i];

	for (int i = 1; i < n; i++)
	{
		int key = arr[i];
		int j = i - 1;

		while (j >= 0 && arr[j] > key)
		{
			arr[j + 1] = arr[j];
			j--;
			//printArr(n);
			if (compareArr(n)) {
				check = true;
				break;
			}
			
		}
		arr[j + 1] = key;
		//printArr(n);
		if (compareArr(n)) {
			check = true;
			break;
		}
	}
	if (check)
		cout << 1;
	else
		cout << 0;

	return 0;
}